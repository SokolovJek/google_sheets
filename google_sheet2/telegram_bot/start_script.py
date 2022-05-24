from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config
import gspread
import requests
from sqlalchemy import create_engine, Integer, Column, Date
import datetime
from telebot import TeleBot
import time


def bot_sent_message(token_bot, id_chat, message_to_send):
    """
    Функция отправляет указанное письмо в указаный чат Telegram.
    :param token_bot: токен бота
    :param id_chat: id чата
    :param message_to_send: текст для отправки
    :return: отправка письма
    """
    bot = TeleBot(token_bot)
    bot.send_message(int(id_chat), message_to_send)


def convert_date(date):
    """
    Функция преобразует дату, для записи в БД.
    :param date: 13.05.2022
    :return 2022-05-13
    """
    date = date.split('.')
    return f'{date[2]}-{date[1]}-{date[0]}'


def dollar_exchange_rate(usd, exchange_rate_usd):
    """
    Конвертер валют. Делает запрос для получения курса и конвертирует долары в рубли.
    :param usd: количество доларов
    :param exchange_rate_usd: курс доллара
    :return: рубли
    """
    rub = usd * exchange_rate_usd
    return round(rub)


Base = declarative_base()


class Orders(Base):
    __tablename__ = 'my_app_orders'

    id = Column(Integer, primary_key=True)
    order = Column(Integer, nullable=False)
    prise_usd = Column(Integer, nullable=False)
    delivery_time = Column(Date)
    price_ru = Column(Integer, nullable=False)

    def __repr__(self):
        return "<my_app_orders(id='%s', order='%s', prise_usd='%s',delivery_time='%s', price_ru='%s')>" % (
            self.id, self.order, self.prise_usd, self.delivery_time, self.price_ru,)


# Создание объекта Session
engine = create_engine(config.patch_to_table)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)  # создание таблици

while True:
    # запрос в google_sheets
    gc = gspread.service_account(filename=config.credentials_file)
    gsheet = gc.open_by_key(config.file_id)
    mydata = gsheet.sheet1.get_all_records()

    # запрос для получения курса
    exchange_rate = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    exchange_rate = exchange_rate['Valute']['USD']['Value']

    # обработка даты
    now_data = str(datetime.date.today())
    now_data_format = time.strptime(now_data, "%Y-%m-%d")

    if session.query(Orders).count() == 0:
        for i in mydata:
            delivery_time = convert_date(i['срок поставки'])
            prise_usd = i['стоимость,$']

            # отпрака ботом уведомления
            if time.strptime(delivery_time, "%Y-%m-%d") < now_data_format:
                bot_sent_message(token_bot=config.token,
                                 id_chat=config.chat_id,
                                 message_to_send=f"Просрочена отправка заказа №{i['заказ №']}")

            session.add(Orders(order=i['заказ №'],
                               prise_usd=prise_usd,
                               delivery_time=delivery_time,
                               price_ru=dollar_exchange_rate(prise_usd, exchange_rate)))

        session.commit()

    else:
        for i in mydata:
            delivery_time = convert_date(i['срок поставки'])
            prise_usd = i['стоимость,$']

            # отпрака ботом уведомления
            if time.strptime(delivery_time, "%Y-%m-%d") < now_data_format:
                bot_sent_message(token_bot=config.token,
                                 id_chat=config.chat_id,
                                 message_to_send=f"Просрочена отправка заказа №{i['заказ №']}")

            session.query(Orders). \
                filter(Orders.order == i['заказ №']). \
                update({'order': i['заказ №'],
                        'prise_usd': prise_usd,
                        'delivery_time': delivery_time,
                        'price_ru': dollar_exchange_rate(prise_usd, exchange_rate)})
        session.commit()

    time.sleep(120)

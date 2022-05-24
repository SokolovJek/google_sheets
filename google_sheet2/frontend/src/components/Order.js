import React from 'react'


const OrderItem = ({order}) => {
    return (
        <tr>
            <td>
                {order.order}
            </td>
            <td>
                {order.prise_usd}
            </td>
            <td>
                {order.price_ru}
            </td>
            <td>
                {order.delivery_time}
            </td>
        </tr>
    )
}


const OrdersList = ({orders}) => {
    return (
        <table>
            <th>
                order
            </th>
            <th>
                price_usd
            </th>
            <th>
                price_ru
            </th>
            <th>
                delivery_time
            </th>
            {orders.map((order) => <OrderItem order={order} />)}
        </table>
    )
}

export default OrdersList
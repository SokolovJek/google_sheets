import React from 'react';
import './App.css';
import OrdersList from './components/Order.js'
import axios from 'axios'
import Chart from './components/Chart.js'



class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'orders': []
        }
    }



    componentDidMount() {

        axios.get('http://192.168.0.19:8000/api/drf_data_table/')
            .then(response => {
                const orders = response.data
                this.setState(
                    {
                    'orders': orders
                    }
                )
            }).catch(error => console.log('my' + error))

    }



    render () {
        return (
            <div>
                <div>
                    Main App
                </div>
                <OrdersList orders={this.state.orders} />
                <Chart/>
            </div>
        )
    }
}

export default App;
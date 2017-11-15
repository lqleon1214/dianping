import React from 'react'
import PureRenderMixin from 'react-addons-pure-render-mixin'
import { getOrderListData, postComment } from '../../../fetch/user/orderlist'
import './style.less'
import OrderListComponent from '../../../components/OrderList'

class OrderList extends React.Component {
    constructor(props, context) {
        super(props, context)
        this.shouldComponentUpdate = PureRenderMixin.shouldComponentUpdate.bind(this)
        this.state = {
            data: []
        }
    }
    render() {
        return (
            <div className="order-list-container">
                <h2>您的订单</h2>
                {
                    this.state.data.length
                    ? <OrderListComponent data={this.state.data} submitComment={this.submitComment.bind(this)}/>
                    : <div>加载中...</div>
                }
            </div>
        )
    }
    componentDidMount() {
        // 获取订单信息
        const username = this.props.username
        if (username) {
            this.loadOrderList(username)
        }
    }
    loadOrderList(username) {
        const result = getOrderListData(username)
        result.then((res) => {
            return res.json()
        }).then(json => {
            this.setState({
                data: json
            })
        })
    }
    submitComment(id, value, callback) {
        // 提交评价
        const result = postComment(id, value)
        result.then(res => {
            return res.json()
        }).then(json => {
            if (json.errno === 0) {
                // 已经评价，修改状态成功
                callback()
            }
        })
    }
}

export default OrderList
import React from 'react'
import PureRenderMixin from 'react-addons-pure-render-mixin'
import BuyAndStore from '../../../components/BuyAndStore'
import { connect } from 'react-redux'
import { bindActionCreators } from 'redux'
import { hashHistory } from 'react-router'
import * as storeActionsFromFile from '../../../actions/store'

class Buy extends React.Component {
    constructor(props, context) {
        super(props, context)
        this.shouldComponentUpdate = PureRenderMixin.shouldComponentUpdate.bind(this)
        this.state = {
            isStore: false
        }
    }
    render() {
        return (
            <div>
                <BuyAndStore isStore={this.state.isStore} buyHandle={this.buyHandle.bind(this)} storeHandle={this.storeHandle.bind(this)}/>
            </div>
        )
    }
    componentDidMount() {
        this.checkStoreState()
    }
    checkStoreState() {
        // 检验当前商户是否被收藏
        const id = this.props.id
        const store = this.props.store
        // some的意思是只要对一个满足即可
        store.some(item => {
            if (item.id === id) {
                this.setState({
                    isStore:true
                })
                // 跳出循环
                return true
            }
        })
    }
    buyHandle() {
        // 购买事件
        // 验证登录
        const loginFlag = this.loginCheck()
        if (!loginFlag) {
            return
        }
        // 购买的流程

        // 跳转到用户主页
        hashHistory.push('/user')
    }
    storeHandle() {
        // 收藏事件
        // 验证登录
        const loginFlag = this.loginCheck()
        if (!loginFlag) {
            return
        }

        const id = this.props.id
        const storeActions = this.props.storeActions
        if (this.state.isStore) {
            // 当前商户已经被收藏，点击时即要取消收藏
            storeActions.rm({id: id})
        } else {
            // 当前商户尚未被收藏，点击即进行收藏
            storeActions.add({id: id})
        }

        // 修改状态
        this.setState({
            isStore: !this.state.isStore
        })
    }
    loginCheck() {
        // 验证登录
        const id = this.props.id
        const userinfo = this.props.userinfo
        if (!userinfo.username) {
            // 没有登录，跳转到登录页面
            hashHistory.push('/login/' + encodeURIComponent('/detail/' + id ))
            return false
        }
        return true
    }
}

function mapStateToProps(state) {
    return {
        userinfo: state.userinfo,
        store: state.store
    }
}

function mapDispatchToProps(dispatch) {
    return {
        storeActions: bindActionCreators(storeActionsFromFile, dispatch)
    }
}

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(Buy)
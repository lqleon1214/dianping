import React from 'react'
import PureRenderMixin from 'react-addons-pure-render-mixin'
import { getListData } from '../../../fetch/home/home'
import ListComponent from '../../../components/List'
import LoadMore from '../../../components/LoadMore'

import './style.less'

class List extends React.Component {
    constructor(props, context) {
        super(props, context)
        this.shouldComponentUpdate = PureRenderMixin.shouldComponentUpdate.bind(this)
        this.state = {
            data: [],               // 存储列表信息
            hasMore: false,         // 记录当前状态下，还有没有更多多的数据可供加载
            isLoadingMore: false,   // 记录当前状态下，是"加载中..."还是"点击加载更多"
            page: 1                 // 下一页的页码
        }
    }

    render() {
        return (
            <div>
                <h2 className="home-list-title">猜你喜欢</h2>
                <div>
                    {
                        this.state.data.length
                        ? <ListComponent data={this.state.data}/>
                        : <div>加载中...</div>
                    }
                    {
                        this.state.hasMore && <LoadMore
                            loadMoreFn={this.loadMoreData.bind(this)}
                            isLoadingMore={this.state.isLoadingMore}/>
                    }
                </div>
            </div>
        )
    }

    componentDidMount() {
        //获取首页数据
        this.loadFirstPageData()
    }
    loadFirstPageData() {
        //获取首屏数据
        const cityName = this.props.cityName
        const result = getListData(cityName, 0)
        this.resultHandle(result)
    }
    loadMoreData() {
        //加载更多数据
        // 首先记录状态
        this.setState({
            isLoadingMore: true
        })
        const cityName = this.props.cityName
        const page = this.state.page
        const result = getListData(cityName, page)
        this.resultHandle(result)

        // 增加page的计数
        this.setState({
            page: page + 1,
            isLoadingMore: false
        })
    }
    resultHandle(result) {
        //数据处理
        result.then((res) => {
            return res.json()
        }).then((json) => {
            const hasMore = json.hasMore
            const data = json.data

            // 存储
            this.setState({
                hasMore: hasMore,
                data: this.state.data.concat(data)
            })
        })
    }
}

export default List
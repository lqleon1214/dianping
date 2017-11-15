import React from 'react'
import PureRenderMixin from 'react-addons-pure-render-mixin'
import { getInfoData } from '../../../fetch/detail/detail'
import DetailInfo from '../../../components/DetailInfo'

class Info extends React.Component {
    constructor(props, context) {
        super(props, context)
        this.shouldComponentUpdate = PureRenderMixin.shouldComponentUpdate.bind(this)
        this.state = {
            loadedInfo: false,
            info: {}
        }
    }
    render() {
        return (
            <div>
                {
                    this.state.loadedInfo
                    ? <DetailInfo data={this.state.info}/>
                    : ''
                }
            </div>
        )
    }
    componentDidMount() {
        const id = this.props.id
        const result = getInfoData(id)
        result.then((res) => {
            return res.json()
        }).then(json => {
            this.setState({
                info: json,
                loadedInfo: true
            })
        })
    }
}

export default Info
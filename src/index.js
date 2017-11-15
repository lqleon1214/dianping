import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import registerServiceWorker from './registerServiceWorker';
import { hashHistory } from 'react-router'
import './static/css/common.less'
import './static/css/font.css'
import RouterMap from './router/routeMap'
import configureStore from './store/configureStore'
import { Provider } from 'react-redux'

// 创建 Redux的Store对象
const store = configureStore()

ReactDOM.render(
    <Provider store={store}>
        <RouterMap history={hashHistory}/>
    </Provider>,
    document.getElementById('root'));
registerServiceWorker();

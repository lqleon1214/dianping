import { createStore } from 'redux'
import rootReducer from '../reducers'

export default function configureStore(initialState) {
    const store = createStore(rootReducer, initialState,
        // 触发redux-tool
        window.devToolsExtension ? window.devToolsExtension() : undefined
    )
    return store
}
import { get } from '../get'
import { post } from '../post'

export function getOrderListData(username) {
    const result = get('http://localhost:5000/api/orderlist/' + username)
    return result
}

export function postComment(id, comment) {
    const result = post('http://localhost:5000/api/submitComment/', {
        id: id,
        comment: comment
    })
    return result
}
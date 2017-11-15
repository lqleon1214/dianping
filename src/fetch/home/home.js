import { get } from '../get'

export function getAdData() {
    const result = get('http://localhost:5000/api/homead')
    return result
}

export function getListData(city, page) {
    const result = get('http://localhost:5000/api/homelist/' + encodeURIComponent(city) + '/' + page)
    return result
}
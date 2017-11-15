import { get } from '../get'

// 获取商户详情
export function getInfoData(id) {
    const result = get('http://localhost:5000/api/detail/info/' + id)
    return result
}

// 获取评论数据
export function getCommentData(page, id) {
    const result = get('http://localhost:5000/api/detail/comment/' + page + '/' + id)
    return result
}
from flask import Flask, jsonify, request
from flask_cors import *
import datetime
import random

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/homead/')
def home_ad():
    t = [
        {
            'title': '暑假5折',
            'img': 'http://images2015.cnblogs.com/blog/138012/201610/138012-20161016191639092-2000037796.png',
            'link': 'http://www.imooc.com/wap/index'
        },
        {
            'title': '特价出国',
            'img': 'http://images2015.cnblogs.com/blog/138012/201610/138012-20161016191648124-298129318.png',
            'link': 'http://www.imooc.com/wap/index'
        },
        {
            'title': '亮亮车',
            'img': 'http://images2015.cnblogs.com/blog/138012/201610/138012-20161016191653983-1962772127.png',
            'link': 'http://www.imooc.com/wap/index'
        },
        {
            'title': '学钢琴',
            'img': 'http://images2015.cnblogs.com/blog/138012/201610/138012-20161016191700420-1584459466.png',
            'link': 'http://www.imooc.com/wap/index'
        },
        {
            'title': '电影',
            'img': 'http://images2015.cnblogs.com/blog/138012/201610/138012-20161016191706733-367929553.png',
            'link': 'http://www.imooc.com/wap/index'
        },
        {
            'title': '旅游热线',
            'img': 'http://images2015.cnblogs.com/blog/138012/201610/138012-20161016191713186-495002222.png',
            'link': 'http://www.imooc.com/wap/index'
        }
    ]
    return jsonify(t)


@app.route('/api/homelist/<city>/<int:page>/')
def homelist(city, page=1):
    print(city)
    result = {
        "hasMore": True,
        "data": [
            {
                "img": 'http://images2015.cnblogs.com/blog/138012/201610/138012-20161016201638030-473660627.png',
                "title": '汉堡大大',
                "subTitle": '叫我汉堡大大，还你多彩口味',
                "price": '28',
                "distance": '120m',
                "mumber": '389',
                'id': int(random.random() * 100000)
            },
            {
                "img": 'http://images2015.cnblogs.com/blog/138012/201610/138012-20161016201645858-1342445625.png',
                "title": '北京开源饭店',
                "subTitle": '[望京]自助晚餐',
                "price": '98',
                "distance": '140m',
                "mumber": '689',
                'id': int(random.random() * 100000)
            },
            {
                "img": 'http://images2015.cnblogs.com/blog/138012/201610/138012-20161016201652952-1050532278.png',
                "title": '服装定制',
                "subTitle": '原价xx元，现价xx元，可修改一次',
                "price": '1980',
                "distance": '160',
                "mumber": '106',
                'id': int(random.random() * 100000)
            },
            {
                "img": 'http://images2015.cnblogs.com/blog/138012/201610/138012-20161016201700186-1351787273.png',
                "title": '婚纱摄影',
                "subTitle": '免费试穿，拍照留念',
                "price": '2899',
                "distance": '160',
                "mumber": '58',
                'id': int(random.random() * 100000)
            },
            {
                "img": 'http://images2015.cnblogs.com/blog/138012/201610/138012-20161016201708124-1116595594.png',
                "title": '麻辣串串烧',
                "subTitle": '双人免费套餐等你抢购',
                "price": '0',
                "distance": '160',
                "mumber": '1426',
                'id': int(random.random() * 100000)
            }
        ]
    }
    return jsonify(result)


@app.route('/api/search/<int:page>/<city>/<category>/')
@app.route('/api/search/<int:page>/<city>/<category>/<keyword>/')
def searchList(city, category, keyword='', page=0):
    result = {
        "hasMore": True,
        "data": [
            {
                "img": 'http://images2015.cnblogs.com/blog/138012/201610/138012-20161022145742279-606202974.jpg',
                "title": '河束人家',
                "subTitle": '南锣鼓巷店',
                "price": '150',
                "distance": '120m',
                "mumber": '389',
                'id': int(random.random()*100000)
            },
            {
                "img": 'http://images2015.cnblogs.com/blog/138012/201610/138012-20161022145750123-1745839503.jpg',
                "title": '漫漫火锅',
                "subTitle": '[王府井]自助火锅',
                "price": '113',
                "distance": '140m',
                "mumber": '689',
                'id': int(random.random() * 100000)
            },
            {
                "img": 'http://images2015.cnblogs.com/blog/138012/201610/138012-20161022145755545-1770557408.jpg',
                "title": '北方涮肉',
                "subTitle": '什刹海店',
                "price": '92',
                "distance": '160',
                "mumber": '106',
                'id': int(random.random() * 100000)
            },
            {
                "img": 'http://images2015.cnblogs.com/blog/138012/201610/138012-20161022145800732-576947550.jpg',
                "title": '姓高火锅',
                "subTitle": '知春里店',
                "price": '90',
                "distance": '160',
                "mumber": '58',
                'id': int(random.random() * 100000)
            },
            {
                "img": 'http://images2015.cnblogs.com/blog/138012/201610/138012-20161022145806201-1193851669.jpg',
                "title": '八重牛府',
                "subTitle": '最好吃的牛丸',
                "price": '85',
                "distance": '160',
                "mumber": '1426',
                'id': int(random.random() * 100000)
            },
            {
                "img": 'http://images2015.cnblogs.com/blog/138012/201610/138012-20161022150855185-1659375763.jpg',
                "title": '蜀乡涮锅',
                "subTitle": '[王府井]自助火锅',
                "price": '113',
                "distance": '140m',
                "mumber": '689',
                'id': int(random.random() * 100000)
            },
            {
                "img": 'http://images2015.cnblogs.com/blog/138012/201610/138012-20161022145800732-576947550.jpg',
                "title": '满楼福火锅',
                "subTitle": '知春路店',
                "price": '90',
                "distance": '160',
                "mumber": '58',
                'id': int(random.random() * 100000)
            }
        ]
    }
    return jsonify(result)


@app.route('/api/detail/info/<int:id>/')
def infoDetail(id):
    result = {
        "img": 'http://images2015.cnblogs.com/blog/138012/201610/138012-20161016201645858-1342445625.png',
        "title": '天下第一锅',
        "star": 4,
        "price": '88',
        "subTitle": '重庆 & 四川 麻辣火锅',
        "desc": '营业时间 11:00 - 21:00 <br> 电话订购 11:00 - 19:00 <br> 网络订购 11:00 - 19:00'
    }
    return jsonify(result)


@app.route('/api/detail/comment/<int:page>/<id>/')
def commentDetail(id, page=0):
    result = {
        "hasMore": True,
        "data": [
            {
                "username": '133****3355',
                "comment": '非常好吃，棒棒的，下次再来',
                "star": 5
            },
            {
                "username": '135****3452',
                "comment": '羊肉够分量，不错',
                "star": 4
            },
            {
                "username": '137****1242',
                "comment": '有自助的水果，非常喜欢',
                "star": 4
            },
            {
                "username": '131****3980',
                "comment": '桌子环境有点糟糕，不喜欢',
                "star": 2
            },
            {
                "username": '135****3565',
                "comment": '基本还可以，中规中矩吧，虽然没有啥惊喜',
                "star": 3
            },
            {
                "username": '130****9879',
                "comment": '感觉很棒，服务员态度非常好',
                "star": 5
            },
            {
                "username": '186****7570',
                "comment": '要是能多给开点发票就好了，哈哈啊',
                "star": 4
            }
        ]
    }
    return jsonify(result)


@app.route('/api/orderlist/<username>/')
def orderList(username):
    result = [
        {
            "id": int(random.random() * 100000),
            "img": 'http://images2015.cnblogs.com/blog/138012/201610/138012-20161016201638030-473660627.png',
            "title": '汉堡大王',
            "count": 3,
            "price": '167',
            "commentState": 0
        },
        {
            "id": int(random.random() * 100000),
            "img": 'http://images2015.cnblogs.com/blog/138012/201610/138012-20161016201708124-1116595594.png',
            "title": '麻辣香锅',
            "count": 1,
            "price": '188',
            "commentState": 0
        },
        {
            "id": int(random.random() * 100000),
            "img": 'http://images2015.cnblogs.com/blog/138012/201610/138012-20161016201645858-1342445625.png',
            "title": '好吃自出餐',
            "count": 2,
            "price": '110',
            "commentState": 2
        }
    ]
    return jsonify(result)


@app.route('/api/submitComment/', methods=['GET', 'POST'])
def postComment():
    if request.method == 'POST':
        id = request.form.get('id')
        comment = request.form.get('comment')
        print('id:' + id + ',comment:' + comment)
    result = {
        'errno': 0
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

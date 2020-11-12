from aiohttp import ClientSession
import asyncio

from lxml import etree


async def Qfang_one():
    url = "https://shenzhen.qfang.com/sale/f1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
        "Cookie": "language=SIMPLIFIED; sid=040615b1-f2d0-4409-80d3-a9c21f08a761; JSESSIONID=aaaz1g7iUQv1-b5Xg63wx; cookieId=c2aaacd4-bbce-4734-bc1b-4fb6b56f0753; qchatid=415da884-6a91-4824-9513-e0e12a4a11ab; cookieId=e693e6d0-d6d4-4a6d-8223-fb4a067cf688; Hm_lvt_4d7fad96f5f1077431b1e8d8d8b0f1ab=1605146958; WINDOW_DEVICE_PIXEL_RATIO=1.125; CITY_NAME=SHENZHEN; wzws_cid=c973e165d096271d9cf5f8d4bcae446fbab5a2cbc6b56f9ce5377e9ade78a8ebe3d49e8646a4c41f5a0ae50ffc0f98f8993bdf8e6f68cefbe85a1496acbcc73ea7c4a9f6f6062f8eddb0074bfa5f39c9; Hm_lpvt_4d7fad96f5f1077431b1e8d8d8b0f1ab=1605152155"
    }
    async with ClientSession as session:
        async with session.get(url=url, headers=headers) as r:
            html = etree.HTML(r.text)
            # 房子标题
            x1 = html.xpath('//div[@class="list-main-header clearfix"]/a/text()')
            # 房子格式
            x2 = html.xpath('//div[@class="house-metas clearfix"]/p[@class="meta-items"][1]/text()')
            # 房子大小
            x3 = html.xpath('//div[@class="house-metas clearfix"]/p[@class="meta-items"][2]/text()')
            # 房子楼层
            x4 = html.xpath('//div[@class="house-metas clearfix"]/p[@class="meta-items"][4]/text()')
            # 房子朝向
            x5 = html.xpath('//div[@class="house-metas clearfix"]/p[@class="meta-items"][5]/text()')
            # 房子年份
            x6 = html.xpath('//div[@class="house-metas clearfix"]/p[@class="meta-items"][6]/text()')
            # 房子位置
            x7 = html.xpath('//div[@class="text fl"]/a/following-sibling::node()/text()')
            # 房子附近（注意：整个标签需要解析）
            x8 = html.xpath('//div[@class="house-tags clearfix"]')
            # 房子价格（万）
            x9 = html.xpath('//div[@class="list-price"]/p/span[1]/text()')
            # 每平方价格
            x10 = html.xpath('//div[@class="list-price"]/p[2]/text()')

            for temp in x1:
                item = dict()
                item["房子标题"] = temp
                item["房子格式"] = x2[x1.index(temp)]
                item["房子大小"] = x3[x1.index(temp)]
                item["房子楼层"] = x4[x1.index(temp)]
                item["房子朝向"] = x5[x1.index(temp)]
                item["房子年份"] = x6[x1.index(temp)]
                item["房子位置"] = x7[x1.index(temp)]
                str = ""
                t1 = temp.xpan(".//text()")
                for i in t1:
                    # 去除换行和空格
                    i = i.replace('\n', '')
                    i = i.replace('\t', '')
                    # 将过滤出来的文本放进上面创建的字符串中
                    str += i
                print(str)
                item["房子附近"] = x8[x1.index(temp)]
                print(item)
                item["房子价格（万）"] = x9[x1.index(temp)]
                item["每平方价格"] = x10[x1.index(temp)]

            # async await 返回值


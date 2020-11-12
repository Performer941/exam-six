import csv
import time
import requests
from lxml import etree


def main(url, headers):
    r = requests.get(url=url, headers=headers)

    html = etree.HTML(r.text)
    # 汽车标题
    x1 = html.xpath('//ul[@class="carlist clearfix js-top"]/li/a/h2/text()')
    # 汽车年份
    x2 = html.xpath('//div[@class="t-i"]/text()[1]')
    # 汽车公里数
    x3 = html.xpath('//div[@class="t-i"]/text()[2]')
    # 汽车价格   (注意：整个标签)
    x4 = html.xpath('//div[@class="t-price"]/p/text()[1]')

    for temp in x1:
        item = dict()
        item["汽车标题"] = temp
        item["汽车年份"] = x2[x1.index(temp)]
        item["汽车公里数"] = x3[x1.index(temp)]
        item["汽车价格(万)"] = x4[x1.index(temp)]
        print(item)

        with open("test.csv", "a") as f:
            list1 = list()
            list1 += item
            # print("1",list1)
            t_csv = csv.DictWriter(f, list1)
            # t_csv.writeheader()
            list1 = [item]
            t_csv.writerows(list1)


# 捕获异常
def trys(url, headers):
    try:
        main(url, headers)
        r = '成功爬取'
        return r
    except Exception as ret:
        print(ret)
        r = "被发现啦"
        return r


if __name__ == '__main__':
    for i in range(1, 11):
        time.sleep(2)
        url = "https://www.guazi.com/suqian/dazhong/o%s" % i

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
            "Cookie": "antipas=654723339Z87387259eT3xU397; uuid=3503f9d6-10a0-4453-f3e1-c0e805a7ab27; cityDomain=suqian; clueSourceCode=%2A%2300; user_city_id=292; ganji_uuid=4754844755627927141218; sessionid=44545f54-6b51-4bd1-a639-4058d99da208; lg=1; Hm_lvt_bf3ee5b290ce731c7a4ce7a617256354=1605140249; close_finance_popup=2020-11-12; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22default%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%223503f9d6-10a0-4453-f3e1-c0e805a7ab27%22%2C%22ca_city%22%3A%22suqian%22%2C%22sessionid%22%3A%2244545f54-6b51-4bd1-a639-4058d99da208%22%7D; preTime=%7B%22last%22%3A1605140374%2C%22this%22%3A1605140247%2C%22pre%22%3A1605140247%7D; Hm_lpvt_bf3ee5b290ce731c7a4ce7a617256354=1605140375"
        }
        r = trys(url, headers)

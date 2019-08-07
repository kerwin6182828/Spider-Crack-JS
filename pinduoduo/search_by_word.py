import requests
import execjs
import re
session = requests.session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
}

with open('0805.js', 'r', encoding='utf-8') as f:
    anti_js = f.read()

ctx = execjs.compile(anti_js)

r = session.get('http://mobile.yangkeduo.com/search_result.html?search_key=衣服', headers=headers)
print(r.text)
list_id = re.search('"listID":"([^"]+)"', r.text).group(1)
flip = re.search('"flip":"([^"]+)"', r.text).group(1)


anti = ctx.call('get_anti', "http://mobile.yangkeduo.com/search_result.html?search_key=%E8%A1%A3%E6%9C%8D&search_src=history&search_met=history_sort&search_met_track=history&refer_search_met_pos=0&refer_page_name=search&refer_page_id=10031_1565068587591_krWpAI94kc&refer_page_sn=10031")

headers['referer'] = "http://mobile.yangkeduo.com/search_result.html?search_key=%E8%A1%A3%E6%9C%8D&search_src=history&search_met=history_sort&search_met_track=history&refer_search_met_pos=0&refer_page_name=search&refer_page_id=10031_1565068587591_krWpAI94kc&refer_page_sn=10031"
response = session.get("http://mobile.yangkeduo.com/proxy/api/search?source=search&list_id=" + list_id + "&sort=default&q=%E8%A1%A3%E6%9C%8D&page=2&size=50&flip=" + flip + "&anti_content=" + anti, headers=headers)
print("http://mobile.yangkeduo.com/proxy/api/search?source=search&search_met=history&track_data=refer_page_id,10031_1565068587591_krWpAI94kc;refer_search_met_pos,0&list_id=lcokY9Gi7D&sort=default&filter=&q=%E8%A1%A3%E6%9C%8D&page=2&size=50&flip=20;4;0;0;05bc3d28-c05d-4b30-b3fa-4949e2861355&anti_content=" + anti)
print(response.text)


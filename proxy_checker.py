import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    else:
        return None

def get_addr_port(html):
	proxy_list=[]
	soup = BeautifulSoup(html,'lxml')
	trs = soup.find_all('tr',class_=['odd','even'])
	for tr in trs:
		value = tr.find('td').text
		proxy_list.append(value)
	return proxy_list

def check_proxy(proxies):
	# print (proxies)
	work_proxy=[]
	for proxy in proxies:
		proxy_check = 'http://' + proxy
		try:
			r = requests.get('http://ya.ru',proxies={'http':proxy_check} )
			print (r.status_code)
			if r.status_code == 200:
				work_proxy.append(proxy)
		except Exception:
			continue
	return work_proxy



def main():
	url='http://www.ip-adress.com/proxy_list/'
	html = get_html(url)
	proxies = get_addr_port(html)
	good_proxies = check_proxy(proxies)
	for proxy in good_proxies:
		print (proxy)

if __name__=='__main__':
	main()
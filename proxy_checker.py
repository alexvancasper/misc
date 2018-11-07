import requests
import datetime
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
    table_tag = soup.find("table", class_="htable proxylist")
    trs = table_tag.find_all('td')
    for tr in trs:
        try:
            addres = tr.find('a').get_text()
            if addres:
                value = tr.get_text()
            proxy_list.append(value)
        except Exception as e:
            continue
    return proxy_list

def check_proxy(proxies):
    work_proxy=[]
    for num, proxy in enumerate(proxies, start=1):
        print ("{}: Checking: {}".format(num, proxy))
        proxy_check = 'http://' + proxy
        try:
            r = requests.get('http://ya.ru',proxies={'http':proxy_check} )
            if r.status_code == 200:
                work_proxy.append(proxy)
        except requests.exceptions.ConnectionError:
            continue
    return work_proxy

def save_to_file(proxies,filename):
    if filename is None:
        filename = datetime.datetime.now().strftime("%Y%m%d")+".txt"
    output = open (filename,'w')
    for proxy in proxies:
        output.write(proxy+"\n")
    print ('Amount:'+str(len(proxies)))

def main():
    url='http://www.ip-adress.com/proxy_list/'
    print ("Requesting url: "+url)
    html = get_html(url)
    if len(html)>200:
        print ("Request from the server was recevied")
    proxies = get_addr_port(html)
    print ("Got: {} proxies".format(len(proxies)))
    good_proxies = check_proxy(proxies)
    print ("Checked: {} proxies are working".format(len(good_proxies)))
    print ("Writing to file")
    save_to_file(good_proxies,'proxies.txt')
    print ('Done')


if __name__=='__main__':
    main()

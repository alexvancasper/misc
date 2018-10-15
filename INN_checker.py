#!/usr/bin/python3.5

import json
import requests
import os
from urllib.parse import urlencode 
from bs4 import BeautifulSoup
from PIL import Image

URL='https://egrul.nalog.ru'
INN = '/home/badcoder/Desktop/inn_uniq.lst'
PDF_PATH = '/home/badcoder/Desktop/pdf/'
CAPTCHA_PATH = '/home/badcoder/Desktop/captcha/'

def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text

def get_file(url):
    r = requests.get(url, stream=True)
    return r

def read_data(file):
    with open(file) as f:
        content = f.read().splitlines()    
    return content

def get_pdf(image_value, file_object):
    global PDF_PATH
    with open(PDF_PATH+image_value+'.pdf', 'bw') as f:
        for chunk in file_object.iter_content(8192):
            f.write(chunk)
    return PDF_PATH+image_value+'.pdf'

def get_image_captha(image_value, file_object):
    global CAPTCHA_PATH
    with open(CAPTCHA_PATH+image_value+'.jpg', 'bw') as f:
        for chunk in file_object.iter_content(8192):
            f.write(chunk)
    return CAPTCHA_PATH+image_value+'.jpg'

def get_captha(html):
    soup = BeautifulSoup(html, 'lxml')
    token_value = soup.find('div', class_='form-field captcha-field').find('input', type="hidden" ).get('value')
    token_image = soup.find('div', class_='form-field captcha-field').find('img').get('src')
    # return token_image.split('&')[0], token_value
    return token_image, token_value

def make_request(data):
    url='https://egrul.nalog.ru/'
    headers = {'content-type': 'application/x-www-form-urlencoded',
               'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Accept-Encoding':'gzip, deflate, br',
               'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
               'User-Agent':'Chrome/67.0.3396.99 Safari/537.36',
               'X-Requested-With': 'XMLHttpRequest',
               'Origin': 'https://egrul.nalog.ru',
               'Connection': 'keep-alive'}
    response = requests.post(url, headers=headers, data=urlencode(data))
    json_reponse = json.loads(response.text)
    if response.status_code == 200:
        if "ERRORS" in json_reponse.keys():
            return json_reponse['ERRORS']['captcha'][0]
        return json_reponse
    else:
        print(response.status_code)
        print(response.text)
        return {}

def main():
    global URL, INN
    
    inn_lines = read_data(INN)
    for idx,inn in enumerate(inn_lines):
        if idx == 3:
            break
        repeat=True
        while repeat:
            html_code = get_html(URL)
            img_url, img_value = get_captha(html_code)
            image_path = get_image_captha(img_value, get_file(URL+img_url))
            img = Image.open(image_path)
            img.show()
            captcha = input("Enter the captcha: ")
            print("[{}] Requesting INN: {}\tCaptha: {}".format(str(idx+1), inn, captcha))
            kind = 'ul'
            # kind = 'fl'
            query = dict(kind='ul',srchUl='ogrn', ogrninnul=inn, namul='',
            regionul=50, srchFl='ogrn', ogrninnfl='', fam='', nam='', otch='', region='', captcha=captcha, captchaToken=img_value)
            json_reponse = make_request(query)
            if 'rows' in json_reponse.keys():
                print("[{}]\tTotal rows: {}".format(str(idx+1), len(json_reponse['rows'])))
                for idx_row,row in enumerate(json_reponse['rows']):
                    filename = get_pdf(row['INN']+"_"+row['NAME'].replace(' ','_'), get_file(URL+'/download/'+row['T']))
                    print("[{}]\t[{}] PDF downloaded size: {} ".format(str(idx+1), str(idx_row+1), os.stat(filename).st_size ))
                    repeat=False
            else:
                print("Captcha is not correct, need to remember it! INN: {}".format(inn))
                repeat=True
            html_code =''

if __name__=='__main__':
    main()        

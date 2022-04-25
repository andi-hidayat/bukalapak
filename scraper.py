from inspect import Parameter
from nbformat import write
import requests
import csv

key = input('Masukan Keyword Produk: ')
write = csv.writer(open('hasil/{}.csv'.format(key), 'w', newline=''))
thead = ['Nama', 'Harga', 'Stok', 'Link']
write.writerow(thead)

url = 'https://api.bukalapak.com/multistrategy-products'
count = 0
for page in range(1, 11):
    parameter = {
        'keywords': key,
        'limit': 50,
        'offset': 50,
        'facet': True,
        'page': page,
        'shouldUseSeoMultistrategy': False,
        'access_token': 'EM4Ikp5Lu3HhHG7mY_Gbyz1eHOr6Idvj3DdSbZjEa9e0CA',
    }

    res = requests.get(url, params=parameter).json()

    products = res['data']
    for p in products:
        nama = p['name']
        harga = p['price']
        stok = p['stock']
        link = p['url']
        count+=1

        print('No:' ,count, 'nama:',nama, 'harga:',harga, 'stok:',stok,'link:',link,)
        write = csv.writer(open('hasil/{}.csv'.format(key), 'a', newline=''))
        data = [nama, harga, stok, link]
        write.writerow(data)


import requests
from bs4 import BeautifulSoup

res=requests.get('https://joytas.net/kaba/')
res.encoding=res.apparent_encoding
#第１引数にhtml文字列、第２引数にパーサーを指定する。今回は追加ライブラリ不要なhtml.parserを指定
soup=BeautifulSoup(res.text,'html.parser')
#BeautifulSoupオブジェクトをprintにそのまま渡すと全文を表示する
print(soup)

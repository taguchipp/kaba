import requests
from bs4 import BeautifulSoup

res=requests.get('https://joytas.net/kaba/')
res.encoding=res.apparent_encoding
#第１引数にhtml文字列、第２引数にパーサーを指定する。今回は追加ライブラリ不要なhtml.parserを指定
soup=BeautifulSoup(res.text,'html.parser')
#BeautifulSoupオブジェクトをprintにそのまま渡すと全文を表示する
#print(soup)

#タグで要素取得
ele=soup.find('title')#<title>要素
#要素のtextコンテントを表示
print(ele.text)

#要素を結果セットとして取得
imgs=soup.find_all('img')
for img in imgs:
    print(img.get('src'))

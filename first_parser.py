import requests
import re
import time

def download(query):
    start=time.time()
    url=f"https://free-images.com/search/?q={query}&cat=st"
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    value= requests.get(url, headers=headers).text
    parser= value.split(r'src=')
    results=[]
    for item in parser:
        if item.startswith('"/sm/'):
            key= re.search(r'.jpg|.png', item).span()
            results.append('https://free-images.com'+item[1:key[1]])
    print("\n".join(results))
    stop=time.time()-start
    print(stop)
def main():
    query= input("Query ")
    download(query)

main()

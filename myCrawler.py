import requests
from bs4 import BeautifulSoup

def crawler():
    """

    :rtype: object
    """
    global count
    url = "https://ontrava.com"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text , "html.parser")
    #print(plain_text)
    count = 1
    for element in soup.findAll('img' , {'class' : 'img-responsive'}):
        href = element.get('src')
        print (href)
        count += 1
        print(count)

crawler()

        

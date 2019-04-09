# Beautiful Soap

Uso básico

```python
    from bs4 import BeautifulSoup

    arquivo = 'pagina_web.html'

    html_doc = open(arquivo,'r',encoding='utf-8').read() # iso-8859-1 latin-1
    soup = BeautifulSoup(html_doc,'html.parser')

    links = soup.find_all('a',href=True)
    links = soup.find_all('ul',class_='visualNoMarker')
```
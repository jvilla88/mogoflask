from urllib.request import urlopen, Request
import nose.tools as nose_tools
var=True
nose_tools.assert_true(var)


def leer_url(url):
    with urlopen(url) as respuesta:
        return respuesta.read().decode('utf-8')

def main():
    req = Request(
    url='https://www.softpedia.com', 
    headers={'User-Agent': 'Mozilla/5.0'}
)
    codigo_html = leer_url(req)
    print(codigo_html)

if __name__ == '__main__':
    main()
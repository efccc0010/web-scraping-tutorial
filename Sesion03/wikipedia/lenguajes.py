import requests
from lxml import html

# "user agent" cadena de texto donde se identifica
# al navegador y el SO del cliente (ROBOT)

""" 
Para obtener el user-agent en Edge:
1. Click derecho en la página
2. Escogemos Inspeccionar
3. Escogemos RED
4. Refrescamos página
5. Seleccionamos apartado ENCABEZADOS """
encabezados = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57"
}
# guardamos la url de la página
url = "https://www.wikipedia.org/"

# obtener requerimiento
respuesta = requests.get(url,headers=encabezados)

parser = html.fromstring(respuesta.text)

idioma1 = parser.get_element_by_id("js-link-box-es")

# usando lxml
print(idioma1.text_content())

idiomas = parser.find_class('central-featured-lang')
for idioma in idiomas:
    print(idioma.text_content())
# usando xpath
idioma1 = parser.xpath("//a[@id='js-link-box-es']/strong/text()")
print(idioma1)

idiomas = parser.xpath("//div[contains(@class,'central-featured-lang')]//strong/text()")
print(idiomas)
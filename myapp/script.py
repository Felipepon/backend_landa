import requests
from bs4 import BeautifulSoup
from django.core.files.base import ContentFile
from .models import Documento

def descargar_documento_dane():
    url = 'https://www.dane.gov.co/index.php/estadisticas-por-tema/pobreza-y-condiciones-de-vida/pobreza-monetaria'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        links = soup.find_all('a', href=True)
        
        for link in links:
            if 'Anexo pobreza monetaria nacional' in link.text and link['href'].endswith('.xls'):
                archivo_url = link['href']
                archivo_nombre = archivo_url.split('/')[-1]
                
                archivo_response = requests.get(archivo_url)
                if archivo_response.status_code == 200:
                    documento = Documento(nombre=archivo_nombre)
                    documento.archivo.save(archivo_nombre, ContentFile(archivo_response.content))
                    documento.save()
                    print(f"Documento {archivo_nombre} descargado y guardado en la base de datos.")
                else:
                    print("Error al descargar el archivo.")
                break
        else:
            print("No se encontró el archivo especificado.")
    else:
        print("Error al acceder a la página del DANE.")

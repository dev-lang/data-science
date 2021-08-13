from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint as visualizar
import pandas as pd

url = "https://boston.craigslist.org/search/sof"
urlGoogle = "https://google.com"
urlSearch = "https://www.google.com.ar/search?q=search+item"
response = requests.get(url)
bs_num = int(0)


elementos = ['result-title','result-hood','result-info','result','result-date','postingbody','attrgroup']
# 0 = result-title
# 1 = result-hood
# 2 = result-info
# 3 = result
# 4 = result-date
# 5 = postingbody
# 6 = attrgroup

# DIC-PANDAS
d = {'key':'value'}

# DIC-PANDAS
d['new key'] = 'new value'

trabajos = {}

data = response.text

soup = bs(data,'html.parser')

tags = soup.find_all('a')
titles = soup.find_all("a",{"class":elementos[0]})
adresses = soup.find_all("span",{"class":elementos[1]})
jobs = soup.find_all("div",{"class":elementos[2]})

def tagHcHref():
    for tag in tags:
        visualizar(tag.get('href'))

def titlesHc():
    for title in titles:
        visualizar(title.text)

def adressesHc():
    for adress in adresses:
        print(adress.text)

def jobsHc():
    global bs_num
    
    while True:
        for job in jobs:
            titulo_t = job.find("a",{"class":elementos[0]})
            titulo = titulo_t.text if titulo_t else "No encontrado"
            lugar_t = job.find("span",{"class":elementos[1]})
            lugar = lugar_t.text if lugar_t else "No encontrado"
            fecha = job.find("time",{"class":elementos[4]}).text
            enlace = job.find("a",{"class":elementos[0]}).get("href")
            #
            job_response = requests.get(enlace)
            job_data = job_response.text
            job_soup = bs(job_data, 'html.parser')
            job_descr = job_soup.find("section",{"id":elementos[5]}).text
            job_attributes_t = job_soup.find("p",{"class":elementos[6]}) 
            job_attr = job_attributes_t.text if job_attributes_t else "No encontrada"
            bs_num+=1
            trabajos[bs_num] = [titulo, lugar, fecha, enlace, job_attr, job_descr]
            print("Trabajo: ",titulo,"\nLugar:",lugar,"\nFecha:",fecha,"\nLink:",enlace,"\n","\nDescripcion:",job_descr,"\n",job_attr,"\n-----------")
        url_ps = soup.find('a',{'title':'next page'})
        if url_ps.get('href'):
            url = url + url_tag.get('href')
            print("vero", url)
        else:
            break
    print("Total:", bs_num)


#tagHcHref()
#titlesHc()
#adressesHc()
jobsHc()

trabajos_df = pd.DataFrame.from_dict(trabajos, orient = 'index', columns = ['Job Title','Location','Date', 'Link', 'Job Attributes', 'Job Description'])

trabajos_df.head()

trabajos_df.to_csv('trabajos.csv')

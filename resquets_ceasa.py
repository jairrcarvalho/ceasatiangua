import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import tabula
import pandasql as psql


def dataTabela():
    url = 'https://files.ceasa-ce.com.br/unsima/boletim_diario/boletim.php'
    respData = requests.get(url)

    if respData.status_code == 200:
        resphtml = respData.text
        soup = BeautifulSoup(resphtml,'html.parser')
        span_data = soup.find(class_='data_outrodia')
        if span_data:
            return span_data.text
    else:
        return 'erro de acesso'
   


def obterConsulta(linkurl, legume):
    # URL da página que você deseja acessar

    url = linkurl


    # Fazer uma solicitação HTTP para obter o conteúdo da página
    resposta = requests.get(url)

    #Verificando se a requisição foi bem sucedida
    if resposta.status_code  ==  200:

        #lendo o conteudo html
        conteudo_html = resposta.text

        #procurando a div do conteudoe a tag (a)
        soup = BeautifulSoup(conteudo_html, "html.parser")
        tag_div = soup.find(class_= "box2") 
        elementos_tag_div = tag_div.find_all('a')

        #buscando o 7° elemento (li) da div selecionada
        link_hort_tian = elementos_tag_div[6]


            

        #o LINK aponta para um diretorio interno(prescisa juntar com o a url )
        if link_hort_tian:
            href =  link_hort_tian['href']
            absolute_url_pdf = urljoin(url, href)
            
            #requisição a url completa
            resposta_pdf = requests.get(absolute_url_pdf)

            #Verificando se a requisição foi bem sucedida
            if resposta_pdf.status_code == 200:

                #armazenando o conteúdo binário
                conteudo_em_pdf = 'pdf_boletim_tiangua.pdf'
                with open(conteudo_em_pdf, 'wb') as file:
                    file.write(resposta_pdf.content)
                

                tabela = tabula.read_pdf(conteudo_em_pdf,pages='1')[0]

                pysqldf = psql.sqldf
                


                consulta = f"""
                        SELECT  "HORTALIÇAS UND", "MÍN", "MC", "MAX"
                        FROM tabela
                        WHERE  "HORTALIÇAS UND" = '{legume}'
                        """

                
                resultado_consulta = pysqldf(consulta) 
                resultado_consulta_json = resultado_consulta.to_json(orient='records')
  
            else:
                return'Falha ao baixar o PDF. Código de resposta:', resposta_pdf.status_code
                
            
        else:
            
            return 'Falha ao acessar o BOLETIM_INFORMATIVO_CEASA. Código de resposta do erro:', link_hort_tian.status_code

    else:
        return "Página não encontrada"
    
          
    return resultado_consulta_json  

        

# Instalação das bibliotecas que não são nativas no Google Colaboraatory
# !pip install PyPDF2
# !pip install pdfplumber

# Importando as bibliotecas
import os
import pdfplumber
import time
from PyPDF2 import PdfWriter, PdfReader


def pdf_get_name(page, pdf_file):
    # O método open retorna uma instância da classe pdfplumber.PDF.
    pdf_content = pdfplumber.open(pdf_file)

    # Seleciona a página.
    pdf_page = pdf_content.pages[page]

    # Extrai o texto dividido por quebras de linha
    pdf_text = pdf_page.extract_text().split('\n')

    # print(pdf_text)
    # O nome que precisa ser extraído está na posição 4 da lista 'pdf_text'.
    name = pdf_text[2]

    # Limpa o nome extraído removendo alguns números. Para isso é passado um filtro com a função lambda que verifica caractere por caractere.
    # Caso o caractere não esteja em '0123456789', ele é retonado dentro de uma lista.
    name = list(filter(lambda c: c in '0123456789(', name))

    # O método join() une os caracteres em uma única string novamente. Em seguida, remove os espaços em excesso.
    name = ''.join(name).strip()
    name_arr = name.split('(')
    # print(name_arr[0])
    name = name_arr[0]
    return name


def pdf_sep(pdf_file, out_dir):
    # pdf_file é o caminho do pdf orinal
    # out_dir é a pasta onde os pdfs divididos serão salvos

    # Abre o pdf original no modo de leitura
  
    with open(pdf_file, 'rb') as pdf:
        # Cria dois objetos, o primeiro da classe PdfFileReader para leitura e o segundo, da classe PdfFileWriter, para escrita
        pdf_content = PdfReader(pdf_file)

        # Armazena o quantidade de páginas do pdf original
        num_pages = len(pdf_content.pages)
        # print(num_pages)
        # print('---------------------------------')
        # Faz uma iteração para cada uma das páginas
        #for page in range(num_pages):
        for page in range(num_pages):
            pdf_writer = PdfWriter()
            # Adiciona a página da iteração atual ao objeto para escrita do PDF
            pdf_writer.add_page(pdf_content.pages[page])

            # Invoca a função pdf_get_name para extrair o nome contido na página atual
            pdf_name = pdf_get_name(page, pdf_file)

            # print(pdf_name + '.pdf')
            # O médoto os.path.join() une o caminho para gravação, o nome e a extesão do arquivo pdf.
            pdf_out = os.path.join(out_dir, pdf_name + '.pdf')

            # Grava o objeto de escrita no arquivo
            with open(pdf_out, 'wb') as pdf_named:
                pdf_writer.write(pdf_named)




# Caminho para o arquivo original
pdf_file = 'Total.pdf'
# Pasta onde os PDFs serão salvos
out_dir = './holerites'
 
tempo_inicial = time.time()
# Invoca a função separador
pdf_sep(pdf_file, out_dir)
tempo_final = time.time()
#Print do tempo que demorou para rodar a parte específica do código
tempo_total = tempo_final - tempo_inicial
print(tempo_total, 'segundos')
import os
from PyPDF2 import PdfWriter, PdfReader

def pdf_sep(pdf_file, out_dir, rename_func):
    # pdf_file é o caminho do pdf orinal
    # out_dir é a pasta onde os pdfs divididos serão salvos

    # Abre o pdf original no modo de leitura
    with open(pdf_file, 'rb') as pdf:
        # Cria dois objetos, o primeiro da classe PdfFileReader para leitura e o segundo, da classe PdfFileWriter, para escrita
        pdf_content = PdfReader(pdf_file)
     
        # Armazena o quantidade de páginas do pdf original
        num_pages = len(pdf_content.pages)
        # print('---------------------------------')
        # Faz uma iteração para cada uma das páginas
        #for page in range(num_pages):
        for page in range(3):
            pdf_writer = PdfWriter()
            # Adiciona a página da iteração atual ao objeto para escrita do PDF
            pdf_writer.add_page(pdf_content.pages[page])

            # Invoca a função pdf_get_name para extrair o nome contido na página atual
            pdf_name = rename_func(page, pdf_file)

            # print(pdf_name + '.pdf')
            # O médoto os.path.join() une o caminho para gravação, o nome e a extesão do arquivo pdf.
            pdf_out = os.path.join(out_dir, pdf_name + '.pdf')

            # Grava o objeto de escrita no arquivo
            with open(pdf_out, 'wb') as pdf_named:
                pdf_writer.write(pdf_named)
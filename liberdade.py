import pdfplumber
from pathlib import Path
import shutil

# Caminho para o arquivo original
pdf_file = './uploads/Liberdade.pdf'

# Pasta onde os PDFs serão salvos
out_dir = Path('./holerites/liberdade')

if shutil.os.path.exists(out_dir):
    # Exclui todos os arquivos no diretório
    shutil.rmtree(out_dir)

if not out_dir.exists():
    # Cria o diretório se não existir
    out_dir.mkdir(parents=True, exist_ok=True)

def pdf_get_name(page, pdf_file):
    # O método open retorna uma instância da classe pdfplumber.PDF.
    pdf_content = pdfplumber.open(pdf_file)

    # Seleciona a página.
    pdf_page = pdf_content.pages[page]

    # Extrai o texto dividido por quebras de linha
    pdf_text = pdf_page.extract_text().split('\n')

    #print(pdf_text)
    # O nome que precisa ser extraído está na posição 4 da lista 'pdf_text'.
    name = pdf_text[8]

    #print(name)

    # Limpa o nome extraído removendo alguns números. Para isso é passado um filtro com a função lambda que verifica caractere por caractere.
    # Caso o caractere não esteja em '0123456789', ele é retonado dentro de uma lista.
    #name = list(filter(lambda c: c in '0123456789(', name))
    name = name.replace(' ','_')
    #print(name)
    # O método join() une os caracteres em uma única string novamente. Em seguida, remove os espaços em excesso.
    #name = ''.join(name).strip()
    #name_arr = name.split('(')
    # print(name_arr[0])
   # name = name_arr[0]
    return name
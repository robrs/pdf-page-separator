import pdfplumber
from pathlib import Path
import shutil

# Caminho para o arquivo original
pdf_file = './uploads/Total.pdf'

# Pasta onde os PDFs serão salvos
out_dir = Path('./holerites/total')

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
    name = pdf_text[2]

    #print(name)

    # Limpa o nome extraído removendo alguns números. Para isso é passado um filtro com a função lambda que verifica caractere por caractere.
    # Caso o caractere não esteja em '0123456789', ele é retonado dentro de uma lista.
    name1 = list(filter(lambda c: c in '0123456789(', name))
    name2 = list(filter(lambda c: c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ', name))
    #print(name2)
    # O método join() une os caracteres em uma única string novamente. Em seguida, remove os espaços em excesso.
    name1 = ''.join(name1).strip()
    name_arr_1 = name1.split('(')

    name2 = ''.join(name2).strip()
    name2 = name2.replace(' ', '_')
    print(name2)
    name1 = name_arr_1[0]
    #name2 = name_arr_2[0]
    return name1+"_"+name2
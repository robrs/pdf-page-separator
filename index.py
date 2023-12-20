#import total as cliente
import pdf_separator
import importlib

def execute(cliente):
     modulo = importlib.import_module(cliente)
     pdf_separator.pdf_sep(modulo.pdf_file, modulo.out_dir, modulo.pdf_get_name )

execute('liberdade')   
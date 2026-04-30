# utils.py



def _validar_texto(txt):
    return isinstance(txt, str) and len(txt.strip()) > 0
    
def _validar_id(id_curso):
    return isinstance(id_curso, str) and len(id_curso.strip()) > 0


def _validar_nome(nome):
    return isinstance(nome, str) and len(nome.strip()) > 0


def _validar_duracao(duracao):
    return str(duracao).isdigit()

def ler_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: insere um número válido.")
            

def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        print("Erro: texto vazio.")

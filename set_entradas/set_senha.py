from .set_string import verifica_String
import re

# -- Verifica se a Senha é Válida ---
def verificar_Senha():
    while True:
        senha = verifica_String('Senha (Números, Letras e Símbolos): -> ')
        if len(senha) < 6 or len(senha) > 6:
            print('A Senha deve ter 6 caracteres.')
        elif not re.search(r"[A-Z]", senha):
            print("A senha deve ter pelo menos uma letra maiúscula.")
        elif not re.search(r"[0-9]", senha):
            print("A senha deve ter pelo menos um número.")
        elif not re.search(r"[!@#$%^&*()_+=\-]", senha):
            print("A senha deve ter pelo menos um símbolo especial.")
        else: 
            break
    return senha

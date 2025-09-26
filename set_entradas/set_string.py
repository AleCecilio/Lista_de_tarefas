# --- Vefica se a String é Válida ---
def verifica_String(prompt):
    string = input(prompt).strip()
    while string == '':
        print(f'o campo não pode estar vazio!!!')
        string = input(prompt).strip()
    return string

# --- Verifica Float ---
def verificar_Float(prompt):
    while True:
        try:
            valor = float(input(prompt)) 
            break
        except ValueError:
            print('Digite um valor válido')
    
    return valor

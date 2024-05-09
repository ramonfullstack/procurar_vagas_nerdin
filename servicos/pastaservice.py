import tkinter as tk
from tkinter import filedialog

def selecionar_pasta():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    # Abre a janela de seleção de pasta
    pasta_selecionada = filedialog.askdirectory()

    if pasta_selecionada:
        print(f'Pasta selecionada: {pasta_selecionada}')
    else:
        print('Nenhuma pasta selecionada.')
        
    return pasta_selecionada
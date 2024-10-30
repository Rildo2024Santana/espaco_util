# Requisitos:

- Python 3.x
- Biblioteca tkinter para interface gráfica
- Biblioteca pandas para manipulação de dados em Excel
- Biblioteca openpyxl para leitura e escrita em Excel

# Código:

import tkinter as tk
from tkinter import messagebox
import pandas as pd
from openpyxl import load_workbook

# Carregar o arquivo Excel
wb = load_workbook(filename='salas.xlsx')
sheet = wb['Salas']

# Criar a janela principal
root = (link unavailable)()
root.title("Aluguel de Salas")

# Criar os botões
btn_adicionar = tk.Button(root, text="Adicionar Sala", command=lambda: adicionar_sala())
btn_remover = tk.Button(root, text="Remover Sala", command=lambda: remover_sala())
btn_listar = tk.Button(root, text="Listar Salas", command=lambda: listar_salas())
btn_alugar = tk.Button(root, text="Alugar Sala", command=lambda: alugar_sala())
btn_desalugar = tk.Button(root, text="Desalugar Sala", command=lambda: desalugar_sala())

# Criar os labels e entries
label_nome = tk.Label(root, text="Nome da Sala:")
entry_nome = tk.Entry(root)
label_tamanho = tk.Label(root, text="Tamanho da Sala:")
entry_tamanho = tk.Entry(root)
label_capacidade = tk.Label(root, text="Capacidade da Sala:")
entry_capacidade = tk.Entry(root)
label_preco = tk.Label(root, text="Preço da Sala:")
entry_preco = tk.Entry(root)

# Funções para os botões
def adicionar_sala():
    nome = entry_nome.get()
    tamanho = entry_tamanho.get()
    capacidade = entry_capacidade.get()
    preco = entry_preco.get()
    sheet.append([nome, tamanho, capacidade, preco, False])
    wb.save('salas.xlsx')
    messagebox.showinfo("Sucesso", "Sala adicionada com sucesso!")

def remover_sala():
    nome = entry_nome.get()
    for row in sheet.rows:
        if row[0].value == nome:
            sheet.delete_rows(row[0].row)
            wb.save('salas.xlsx')
            messagebox.showinfo("Sucesso", "Sala removida com sucesso!")
            return
    messagebox.showerror("Erro", "Sala não encontrada.")

def listar_salas():
    salas = []
    for row in sheet.rows:
        salas.append([row[0].value, row[1].value, row[2].value, row[3].value, row[4].value])
    messagebox.showinfo("Salas", str(salas))

def alugar_sala():
    nome = entry_nome.get()
    for row in sheet.rows:
        if row[0].value == nome:
            if row[4].value == False:
                row[4].value = True
                wb.save('salas.xlsx')
                messagebox.showinfo("Sucesso", "Sala alugada com sucesso!")
            else:
                messagebox.showerror("Erro", "Sala já está alugada.")
            return
    messagebox.showerror("Erro", "Sala não encontrada.")

def desalugar_sala():
    nome = entry_nome.get()
    for row in sheet.rows:
        if row[0].value == nome:
            if row[4].value == True:
                row[4].value = False
                wb.save('salas.xlsx')
                messagebox.showinfo("Sucesso", "Sala desalugada com sucesso!")
            else:
                messagebox.showerror("Erro", "Sala não está alugada.")
            return
    messagebox.showerror("Erro", "Sala não encontrada.")

# Organizar os widgets
label_nome.grid(row=0, column=0)
entry_nome.grid(row=0, column=1)
label_tamanho.grid(row=1, column=0)
entry_tamanho.grid(row=1, column=1)
label_capacidade.grid(row=2, column=0)
entry_capacidade.grid(row=2, column=1)
label_preco.grid(row=3, column=0)
entry_preco.grid(row=3, column=1)
btn_adicionar.grid(row=4, column=0)
btn_remover.grid(row=4, column=1)
btn_listar.grid(row=5, column=0)
btn_alugar.grid(row=5, column=1)
btn_desalugar.grid(row=6, column=0)


root.mainloop()

# Observações:

#- O arquivo Excel
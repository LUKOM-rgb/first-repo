import tkinter as tk
from tkinter import ttk, messagebox

FILENAME = "presenças.txt"

def consultar_presencas(tree, tipo_movimento, numero):
    """
    Filtra e exibe os dados do ficheiro presenças.txt no Treeview com base nos filtros.
    :param tree: Treeview onde os dados serão exibidos.
    :param tipo_movimento: Filtro de tipo de movimento ('Entrada' ou 'Saída').
    :param numero: Número do aluno para filtrar (ou vazio para todos).
    """
    tree.delete(*tree.get_children())  # Limpar Treeview
    numero = numero.strip()

    try:
        with open(FILENAME, "r") as file:
            for linha in file:
                reg_numero, reg_data, reg_hora, reg_mov = linha.strip().split(";")

                # Aplicar filtros
                if numero and reg_numero != numero:
                    continue
                if tipo_movimento and reg_mov != tipo_movimento:
                    continue

                # Inserir dados filtrados no Treeview
                tree.insert("", "end", values=(reg_numero, reg_data, reg_hora, reg_mov))
    except FileNotFoundError:
        messagebox.showerror("Erro", "Ficheiro de presenças não encontrado!")

# Interface gráfica
root = tk.Tk()
root.title("Gestão de Presenças")
root.geometry("750x500")

# Frames
frame_tipo_movimento = tk.Frame(root, width=220, height=100)
frame_numero = tk.Frame(root, width=220, height=100)
frame_tipo_movimento.grid(row=0, column=0, padx=10, pady=10)
frame_numero.grid(row=0, column=1, padx=10, pady=10)

# Tipo de movimento
tipo_movimento_var = tk.StringVar()
tk.Label(frame_tipo_movimento, text="Tipo de Movimento:").pack()
tk.Radiobutton(frame_tipo_movimento, text="Entrada", variable=tipo_movimento_var, value="Entrada").pack(anchor="w")
tk.Radiobutton(frame_tipo_movimento, text="Saída", variable=tipo_movimento_var, value="Saída").pack(anchor="w")

# Número do aluno
numero_var = tk.StringVar()
tk.Label(frame_numero, text="Número de Aluno:").pack()
tk.Entry(frame_numero, textvariable=numero_var).pack()

# Botão de consulta
imagem_lupa = tk.PhotoImage(file="lupa.png")  # Certifique-se de ter o ficheiro lupa.png no mesmo diretório
tk.Button(root, image=imagem_lupa, width=220, height=100, command=lambda: consultar_presencas(tree, tipo_movimento_var.get(), numero_var.get())).place(x=10, y=120)

# Treeview para exibir os dados
frame_tree = tk.Frame(root, width=690, height=500)
frame_tree.place(x=10, y=160)

columns = ("Número", "Data", "Hora", "Movimento")
tree = ttk.Treeview(frame_tree, columns=columns, show="headings", height=16)
for col, width in zip(columns, [160, 160, 160, 200]):
    tree.heading(col, text=col)
    tree.column(col, width=width)

tree.pack()

root.mainloop()
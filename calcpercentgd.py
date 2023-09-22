import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def calcular_percentual_cor(imagem, baixo, alto):
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    mascara = cv2.inRange(hsv, baixo, alto)
    percentual = (np.sum(mascara > 0) / (imagem.shape[0] * imagem.shape[1])) * 100
    return percentual

def atualizar_percentuais():
    img_path = entrada_caminho_imagem.get()
    img = cv2.imread(img_path)
    vermelho_pct = calcular_percentual_cor(img, vermelho_baixo, vermelho_alto)
    branco_pct = calcular_percentual_cor(img, branco_baixo, branco_alto)
    indefinido_pct = 100 - (vermelho_pct + branco_pct)
    lbl_percentual_vermelho.config(text=f"Percentual vermelho: {vermelho_pct:.2f}%")
    lbl_percentual_branco.config(text=f"Percentual branco: {branco_pct:.2f}%")
    lbl_percentual_indefinido.config(text=f"Percentual indefinido: {indefinido_pct:.2f}%")

def carregar_imagem():
    img_path = entrada_caminho_imagem.get()
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_pil.thumbnail((300, 300))
    img_tk = ImageTk.PhotoImage(img_pil)
    lbl_imagem.config(image=img_tk)
    lbl_imagem.image = img_tk

    # Após carregar a imagem, atualize os percentuais
    atualizar_percentuais()

# Criar a janela principal
janela = tk.Tk()
janela.title("Análise de Imagem")

# Definir os intervalos de cores
vermelho_baixo = np.array([160, 100, 100])
vermelho_alto = np.array([179, 255, 255])
branco_baixo = np.array([0, 0, 200])
branco_alto = np.array([255, 60, 255])

# Criar widgets
lbl_instrucao = ttk.Label(janela, text="Informe o caminho da imagem:")
entrada_caminho_imagem = ttk.Entry(janela, width=50)
btn_carregar = ttk.Button(janela, text="Carregar Imagem", command=carregar_imagem)
lbl_imagem = ttk.Label(janela)
lbl_percentual_vermelho = ttk.Label(janela, text="Percentual vermelho: ")
lbl_percentual_branco = ttk.Label(janela, text="Percentual branco: ")
lbl_percentual_indefinido = ttk.Label(janela, text="Percentual indefinido: ")

# Posicionar widgets
lbl_instrucao.grid(row=0, column=0, columnspan=2)
entrada_caminho_imagem.grid(row=1, column=0, padx=5, pady=5)
btn_carregar.grid(row=1, column=1, padx=5, pady=5)
lbl_imagem.grid(row=2, column=0, columnspan=2)
lbl_percentual_vermelho.grid(row=3, column=0, columnspan=2)
lbl_percentual_branco.grid(row=4, column=0, columnspan=2)
lbl_percentual_indefinido.grid(row=5, column=0, columnspan=2)

# Iniciar a interface
janela.mainloop()

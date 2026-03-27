"""
Exercício 1 - Limiarização
Binarização pixel a pixel com plotagem de histogramas
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Carrega a imagem e converte para escala de cinza
img_colorida = cv2.imread('assets/Tabela.png')
img_cinza = cv2.cvtColor(img_colorida, cv2.COLOR_BGR2GRAY)

# Cria uma cópia para a imagem binarizada
img_binarizada = np.zeros_like(img_cinza)

# Define o limiar para binarização
limiar = 127

# Binarização pixel a pixel
qtdLinhas, qtdColunas = img_cinza.shape
for l in range(qtdLinhas):
    for c in range(qtdColunas):
        if img_cinza[l][c] > limiar:
            img_binarizada[l][c] = 255  # Branco
        else:
            img_binarizada[l][c] = 0    # Preto

# Cria a figura com 2 linhas e 2 colunas
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Exercício 1 - Binarização Pixel a Pixel', fontsize=14)

# Imagem em escala de cinza
axes[0, 0].imshow(img_cinza, cmap='gray')
axes[0, 0].set_title('Imagem em Escala de Cinza')
axes[0, 0].axis('off')

# Histograma da imagem em escala de cinza
axes[0, 1].hist(img_cinza.ravel(), bins=256, range=[0, 256], color='blue', alpha=0.7)
axes[0, 1].set_title('Histograma - Escala de Cinza')
axes[0, 1].set_xlabel('Intensidade de Pixel')
axes[0, 1].set_ylabel('Frequência')
axes[0, 1].axvline(x=limiar, color='red', linestyle='--', label=f'Limiar = {limiar}')
axes[0, 1].legend()

# Imagem binarizada
axes[1, 0].imshow(img_binarizada, cmap='gray')
axes[1, 0].set_title(f'Imagem Binarizada (limiar = {limiar})')
axes[1, 0].axis('off')

# Histograma da imagem binarizada
axes[1, 1].hist(img_binarizada.ravel(), bins=256, range=[0, 256], color='green', alpha=0.7)
axes[1, 1].set_title('Histograma - Imagem Binarizada')
axes[1, 1].set_xlabel('Intensidade de Pixel')
axes[1, 1].set_ylabel('Frequência')

plt.tight_layout()
plt.savefig('resultado_exercicio1.png', dpi=150)
plt.show()

print(f"Dimensões da imagem: {qtdLinhas} x {qtdColunas} pixels")
print(f"Limiar utilizado: {limiar}")
print(f"Pixels brancos (>limiar): {np.sum(img_binarizada == 255)}")
print(f"Pixels pretos (<=limiar): {np.sum(img_binarizada == 0)}")

"""
Exercício 2 - Limiarização
Limiarização TOZERO pixel a pixel com plotagem de histogramas
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Carrega a imagem e converte para escala de cinza
img_colorida = cv2.imread('assets/Arena.jpg')
img_cinza = cv2.cvtColor(img_colorida, cv2.COLOR_BGR2GRAY)

# Cria uma cópia para a imagem limiarizada
img_tozero = np.zeros_like(img_cinza)

# Define o limiar
limiar = 127

# Limiarização TOZERO pixel a pixel
# Se pixel > limiar: mantém o valor original
# Se pixel <= limiar: 0 (preto)
qtdLinhas, qtdColunas = img_cinza.shape
for l in range(qtdLinhas):
    for c in range(qtdColunas):
        if img_cinza[l][c] > limiar:
            img_tozero[l][c] = img_cinza[l][c]  # Mantém valor original
        else:
            img_tozero[l][c] = 0  # Preto

# Cria a figura com 2 linhas e 2 colunas
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Exercício 2 - Limiarização TOZERO Pixel a Pixel', fontsize=14)

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

# Imagem TOZERO
axes[1, 0].imshow(img_tozero, cmap='gray')
axes[1, 0].set_title(f'Imagem TOZERO (limiar = {limiar})')
axes[1, 0].axis('off')

# Histograma da imagem TOZERO
axes[1, 1].hist(img_tozero.ravel(), bins=256, range=[0, 256], color='green', alpha=0.7)
axes[1, 1].set_title('Histograma - Imagem TOZERO')
axes[1, 1].set_xlabel('Intensidade de Pixel')
axes[1, 1].set_ylabel('Frequência')
axes[1, 1].axvline(x=limiar, color='red', linestyle='--', label=f'Limiar = {limiar}')
axes[1, 1].legend()

plt.tight_layout()
plt.savefig('resultado_exercicio2.png', dpi=150)
plt.show()

print(f"Dimensões da imagem: {qtdLinhas} x {qtdColunas} pixels")
print(f"Limiar utilizado: {limiar}")
print(f"Pixels mantidos (>limiar): {np.sum(img_tozero > 0)}")
print(f"Pixels zerados (<=limiar): {np.sum(img_tozero == 0)}")

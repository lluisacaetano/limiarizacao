"""
Exercício 3 - Limiarização
Limiarização multinível invertida pixel a pixel
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Carrega a imagem e converte para escala de cinza
img_colorida = cv2.imread('assets/Raposão.jpg')
img_cinza = cv2.cvtColor(img_colorida, cv2.COLOR_BGR2GRAY)

# Cria uma cópia para a imagem limiarizada
img_multinivel = np.zeros_like(img_cinza)

# Define os limiares
limiar_baixo = 90
limiar_alto = 150

# Limiarização multinível invertida pixel a pixel
# Se pixel < 90: vira 255 (branco) - invertido
# Se pixel > 150: vira 0 (preto) - invertido
# Se pixel entre 90 e 150: mantém valor original
qtdLinhas, qtdColunas = img_cinza.shape
for l in range(qtdLinhas):
    for c in range(qtdColunas):
        if img_cinza[l][c] < limiar_baixo:
            img_multinivel[l][c] = 255  # Invertido: escuro vira branco
        elif img_cinza[l][c] > limiar_alto:
            img_multinivel[l][c] = 0    # Invertido: claro vira preto
        else:
            img_multinivel[l][c] = img_cinza[l][c]  # Mantém original

# Cria a figura com 2 linhas e 2 colunas
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Exercício 3 - Limiarização Multinível Invertida', fontsize=14)

# Imagem em escala de cinza
axes[0, 0].imshow(img_cinza, cmap='gray')
axes[0, 0].set_title('Imagem em Escala de Cinza')
axes[0, 0].axis('off')

# Histograma da imagem em escala de cinza
axes[0, 1].hist(img_cinza.ravel(), bins=256, range=[0, 256], color='blue', alpha=0.7)
axes[0, 1].set_title('Histograma - Escala de Cinza')
axes[0, 1].set_xlabel('Intensidade de Pixel')
axes[0, 1].set_ylabel('Frequência')
axes[0, 1].axvline(x=limiar_baixo, color='red', linestyle='--', label=f'Limiar baixo = {limiar_baixo}')
axes[0, 1].axvline(x=limiar_alto, color='orange', linestyle='--', label=f'Limiar alto = {limiar_alto}')
axes[0, 1].legend()

# Imagem multinível invertida
axes[1, 0].imshow(img_multinivel, cmap='gray')
axes[1, 0].set_title(f'Multinível Invertida ({limiar_baixo} < pixel < {limiar_alto})')
axes[1, 0].axis('off')

# Histograma da imagem multinível
axes[1, 1].hist(img_multinivel.ravel(), bins=256, range=[0, 256], color='green', alpha=0.7)
axes[1, 1].set_title('Histograma - Multinível Invertida')
axes[1, 1].set_xlabel('Intensidade de Pixel')
axes[1, 1].set_ylabel('Frequência')
axes[1, 1].axvline(x=limiar_baixo, color='red', linestyle='--', label=f'Limiar baixo = {limiar_baixo}')
axes[1, 1].axvline(x=limiar_alto, color='orange', linestyle='--', label=f'Limiar alto = {limiar_alto}')
axes[1, 1].legend()

plt.tight_layout()
plt.savefig('resultado_exercicio3.png', dpi=150)
plt.show()

print(f"Dimensões da imagem: {qtdLinhas} x {qtdColunas} pixels")
print(f"Limiares: baixo={limiar_baixo}, alto={limiar_alto}")
print(f"Pixels < {limiar_baixo} (viram 255): {np.sum(img_cinza < limiar_baixo)}")
print(f"Pixels > {limiar_alto} (viram 0): {np.sum(img_cinza > limiar_alto)}")
print(f"Pixels entre {limiar_baixo}-{limiar_alto} (mantidos): {np.sum((img_cinza >= limiar_baixo) & (img_cinza <= limiar_alto))}")

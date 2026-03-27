"""
Exercício 4 - Limiarização
Binarização de vídeo em tempo real
"""

import cv2
import numpy as np

# Abre o vídeo
video = cv2.VideoCapture('assets/GALO.mp4')

# Verifica se o vídeo foi aberto corretamente
if not video.isOpened():
    print("Erro ao abrir o vídeo!")
    exit()

# Define o limiar para binarização
limiar = 127

print("Reproduzindo vídeo binarizado...")
print("Pressione 'q' para sair")
print(f"Limiar: {limiar}")

while True:
    # Lê o próximo frame
    ret, frame = video.read()

    # Se não conseguiu ler (fim do vídeo), reinicia
    if not ret:
        video.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    # Converte para escala de cinza
    frame_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Binarização otimizada com cv2.threshold (muito mais rápido)
    _, frame_binarizado = cv2.threshold(frame_cinza, limiar, 255, cv2.THRESH_BINARY)

    # Mostra o frame original e o binarizado lado a lado
    frame_cinza_rgb = cv2.cvtColor(frame_cinza, cv2.COLOR_GRAY2BGR)
    frame_bin_rgb = cv2.cvtColor(frame_binarizado, cv2.COLOR_GRAY2BGR)

    # Redimensiona para caber na tela
    escala = 0.5
    frame_cinza_rgb = cv2.resize(frame_cinza_rgb, None, fx=escala, fy=escala)
    frame_bin_rgb = cv2.resize(frame_bin_rgb, None, fx=escala, fy=escala)

    # Concatena horizontalmente
    comparacao = np.hstack((frame_cinza_rgb, frame_bin_rgb))

    # Adiciona texto
    cv2.putText(comparacao, 'Original (Cinza)', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(comparacao, f'Binarizado (limiar={limiar})',
                (frame_cinza_rgb.shape[1] + 10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Exibe o frame
    cv2.imshow('Exercicio 4 - Binarizacao de Video', comparacao)

    # Aguarda 30ms e verifica se 'q' foi pressionado
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Libera recursos
video.release()
cv2.destroyAllWindows()
print("Vídeo finalizado!")

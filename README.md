# Limiarização - Visão Computacional

Implementação de técnicas de limiarização (thresholding) em imagens e vídeos usando Python e OpenCV.

## Exercícios

### Exercício 1 - Binarização Simples
Binarização pixel a pixel com plotagem de histogramas.

```python
# Se pixel > limiar: branco (255)
# Se pixel <= limiar: preto (0)
```

### Exercício 2 - Limiarização TOZERO
Mantém valores originais acima do limiar, zera os demais.

```python
# Se pixel > limiar: mantém valor original
# Se pixel <= limiar: 0 (preto)
```

### Exercício 3 - Limiarização Multinível Invertida
Aplica dois limiares com inversão de valores.

```python
# Se pixel < 90: vira 255 (branco)
# Se pixel > 150: vira 0 (preto)
# Se pixel entre 90-150: mantém original
```

### Exercício 4 - Binarização de Vídeo
Binarização em tempo real de vídeo, exibindo comparação lado a lado.

## Estrutura

```
Limiarizacao/
├── assets/
│   ├── Arena.jpg
│   ├── Raposão.jpg
│   ├── Tabela.png
│   └── GALO.mp4
├── exercicio1_limiarizacao.py
├── exercicio2_tozero.py
├── exercicio3_multinivel.py
├── exercicio4_video.py
├── resultado_exercicio1.png
├── resultado_exercicio2.png
└── resultado_exercicio3.png
```

## Requisitos

```bash
pip install opencv-python numpy matplotlib
```

## Uso

```bash
# Exercício 1 - Binarização
python exercicio1_limiarizacao.py

# Exercício 2 - TOZERO
python exercicio2_tozero.py

# Exercício 3 - Multinível
python exercicio3_multinivel.py

# Exercício 4 - Vídeo (pressione 'q' para sair)
python exercicio4_video.py
```

## Conceitos

- **Limiarização**: Técnica de segmentação que separa pixels em classes baseado em valores de intensidade
- **Binarização**: Caso especial com apenas duas classes (preto/branco)
- **Histograma**: Distribuição de frequência dos níveis de intensidade

## Autor

Luisa Caetano - Atividade de Visão Computacional

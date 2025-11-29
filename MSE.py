import os
import cv2
import numpy as np

# Alunos:   André Cristo Valente
#           Nycksandro Lima dos Santos
#           Rômulo Fernandes Torres

# Script para calcular o MSE para todas as 4 imagens de cada objeto em relação a imagem referencial

def calcular_MSE(imagem1, imagem2): # Função para calcular o MSE,comparando a segunda com referência na primeira.
    #Leio as duas imagens, sendo a primeira imagem a de referência, e a segunda a imagem a ser comparada
    imagem_referencia = cv2.imread(diretorio_referencias + imagem1)
    imagem_atual = cv2.imread(diretorio_imagems + imagem2)
    
    #Pego as dimensões das imagens
    largura_referencia, altura_referencia, bandas_referencia = imagem_referencia.shape
    largura_imagem_atual, altura_imagem_atual, bandas_imagem_atual = imagem_atual.shape

    if(altura_referencia != altura_imagem_atual or largura_referencia !=largura_imagem_atual): # Se as dimensões forem diferentes, terei que redimensionar
        print(f"A imagem {imagem2} possuia as dimensões ({largura_imagem_atual}, {altura_imagem_atual}) e foi redimensionado para ({largura_referencia},{altura_referencia}) para realização do cálculo do MSE.")
        if(altura_referencia > altura_imagem_atual or largura_referencia > largura_imagem_atual): # Se for pra aumentar as dimensões, é melhor usar a interpolação
            interpolacao = cv2.INTER_CUBIC
        else: # Se for pra diminuir, é melhor a cv2.INTER_AREA
            interpolacao = cv2.INTER_AREA

        imagem_atual = cv2.resize(imagem_atual, (altura_referencia, largura_referencia), interpolation=interpolacao) # Redimensionando (sempre a segunda imagem)

    # Agora já redimensionando, irei aplicar o calculo

    mse = np.mean((imagem_referencia - imagem_atual) ** 2)# Tô usando numpy para ser mais eficiente. Essa linha equivale a Acumular a diferença ao quadrado de cada pixel e depois dividir pela média
    return mse

diretorio_mse_arq = "mse_arquivo.txt" # Diretório do arquivo que estará o arquivo com os cálculos

diretorio_referencias = "referencias/" # Diretório que está as fotos de referencia

diretorio_imagems = "imagens/" # Diretório que está as imagens

objetos = ["Objeto_01_LA", 
           "Objeto_01_LB",
           "Objeto_02_LA", 
           "Objeto_02_LB", 
           "Objeto_03_LA", 
           "Objeto_03_LB", 
           "Objeto_04_LA", 
           "Objeto_04_LB", 
           "Objeto_05_LA", 
           "Objeto_05_LB"] # Lista substrings que vou usar para quebrar os nomes das imagens em pedaços para facilitar a montagem dos nomes

with open(diretorio_mse_arq, 'w') as mse_arq: # A ideia é criar um arquivo que terá todos os calculos de MSE. Porém, para isso é necessário pegar uma imagem de referência e aplicar o calculo para todas as imagens que irão ser comparadas com ela.
    for obj in objetos: # Pego uma subtring de objeto
        imagem_referencia_atual = None 
        substring_obj = None

        for dir_imagem_ref in os.listdir(diretorio_referencias):
            if (obj in dir_imagem_ref): # Verifico se a substring atual (obj) está na imagem atual (dir_imagem_ref) do diretório das referências. Se tiver eu salvo e vou usar a seguir
                imagem_referencia_atual = dir_imagem_ref
                substring_obj = obj # Nome da imagem
                break # Dou break pois sei que só tem uma imagem de referência para cada configuração

        # Aqui, já tenho o caminho da imagem de referência, falta agora aplicar o calculo para cada uma das imagens que irá ser comparada com ela. Para achar essas imagens, vou buscar no diretorio das imagems cada imagem que possuir a substring atual (obj) e aplicar o calculo do MSE7

        mse_arq.write(f"{substring_obj}:\n\n")

        for dir_imagem_atual in os.listdir(diretorio_imagems):
            if (substring_obj in dir_imagem_atual): # Se a substring está nessa imagem, é por que ela deve ser comparado com a imagem de refêrencia no cálculo.
                imagem_atual = dir_imagem_atual # É apenas o nome da imagem
                mse = calcular_MSE(imagem_referencia_atual, imagem_atual) # Calculo o MSE dentre a imagem de refêrencia e a imagem atual (Já adapto com o caminho)
                mse_arq.write(f"{imagem_atual}: {mse}\n")
        
        mse_arq.write("\n")
    print("Cálculos realizados com sucesso")
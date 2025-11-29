# TP03 de Imagens
## Análise e Tratamento de Imagens e Vídeos Digitais

Nesse repositório está o script para executar e escrever todos os cálculos da métrica MSE (Mean Squared Error) necessários para a realização do experimento do Trabalho Prático da disciplina.

Para reproduzir os cálculos é necessário preparar o ambiente e pastas com as seguintes especificações.

**Importante:** O script foi desenvolvido para calcular apenas de um modelo de uma vez, ou seja, não coloque mais de um modelo na **pasta de imagens**.

### Como preparar o ambiente

Execute os seguintes comandos no terminal do linux para preparar o ambiente.

> git clone https://github.com/Nycksandro/TP03-Imagens     

> cd TP03-Imagens

> mkdir referencias

> mkdir imagens

> python3 -m venv ambiente_venv

> source ambiente_venv/bin/activate

> pip install -r requirements.txt

### **Organização das pastas**
A estrutura do projeto deve ficar da seguinte maneira após a preparação:

    TP03-Imagens/
    │── imagens/
    |── MSE.py
    |── teste.py
    |── referencias/
    │── README.md
    │── requirements.txt

O MSE.py necessita que as pastas sejam dividas da seguinte maneira:

**referencias**: Nessa pasta coloque todas as imagens de referências disponíveis no drive da nossa equipe (Equipe 01).

**imagens:** Nessa pasta coloque todas as imagens que correspondem ao seu modelo de câmera.

### Nome dos arquivos
Para funcionar corretamente, é necessário que as imagens dentro das pastas sigam um padrão (protocolo) de nomeação.

##### Referências

Para as **imagens de referências**, os nomes das imagens devem seguir o padrão: 

> Referencia_Objeto_0X_YY.jpg

Onde X é o **número identificador** do objeto e YY é o **tipo de luz** (LB: Luz Branca e LA: Luz Amarela)

**Exemplo**

> Referencia_Objeto_03_LB.jpg

##### Imagens normais

Para as **imagens normais**, os nomes das imagens devem seguir o padrão:

> Modelo_Objeto_0X_YY_ZZ.jpg

Onde X é o **número identificador** do objeto, YY é o **tipo de luz** (LB: Luz Branca e LA: Luz Amarela) e ZZ é a **intensidade** da luz (AI: Alta Intesidade e BI: Baixa intensidade).

**Exemplo**

> Moto_G_53_Objeto_03_LA_AI.jpg

Após essa divisão e organização, execute o MSE.py, o resultado será um txt (mse_arquivo.txt) contendo todos os cálculos devidamente identificados.

### Notações adotadas para saída

**Exemplo de saída**

    Objeto_01_LA:

    Moto_G_53_Objeto_01_LA_AI.jpg: 105.16201161256268
    Moto_G_53_Objeto_01_LA_BI.jpg: 87.54488333003431

    Objeto_01_LB:

    Moto_G_53_Objeto_01_LB_AI.jpg: 111.24784097057271
    Moto_G_53_Objeto_01_LB_BI.jpg: 115.14491762338348

* **LA:** Luz Amarela
* **LB:** Luz Branca
* **AI:** Alta Intensidade
* **BI:** Baixa Intesidade

    

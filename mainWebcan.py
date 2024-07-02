import cv2
import pickle
import extrairGabarito as exG

# ALTERAR O resp.pkl
# opcoes = [f"{i}-{letra}" for i in range(1, 11) for letra in "ABCDE"]
# with open('resp.pkl', 'wb') as arquivo:
#     pickle.dump(opcoes, arquivo)

# pos = [(30, 12, 54, 41), (97, 13, 50, 38), (162, 15, 52, 36), (226, 12, 52, 37), (288, 14, 55, 35), (31, 55, 50, 33), (96, 54, 53, 38), (163, 55, 52, 38), (225, 57, 55, 33), (294, 55, 54, 37), (29, 95, 51, 40), (95, 97, 55, 38), (163, 96, 53, 38), (230, 97, 52, 37), (294, 97, 58, 36), (27, 139, 54, 37), (96, 138, 54, 40), (158, 141, 61, 36), (229, 141, 59, 38), (298, 139, 57, 37), (24, 181, 55, 43), (95, 186, 56, 37), (163, 186, 60, 35), (231, 182, 60, 39), (301, 183, 61, 40), (21, 233, 59, 34), (91, 231, 61, 35), (161, 229, 64, 40), (235, 229, 57, 40), (306, 228, 56, 40), (20, 278, 57, 39), (91, 278, 60, 38), (164, 277, 62, 38), (234, 275, 64, 40), (307, 274, 62, 41), (17, 329, 61, 40), (89, 330, 62, 39), (166, 324, 61, 47), (241, 324, 61, 43), (313, 324, 62, 44), (17, 380, 57, 43), (88, 382, 65, 43), (169, 378, 63, 47), (242, 376, 65, 48), (318, 377, 64, 44), (10, 439, 66, 42), (89, 435, 63, 43), (166, 434, 66, 45), (246, 433, 65, 49), (324, 432, 63, 45)]


campos = []
with open('campos.pkl', 'rb') as arquivo:
    campos = pickle.load(arquivo)

# Verifica se as opções foram salvas corretamente
resp = []
with open('resp.pkl', 'rb') as arquivo:
    resp = pickle.load(arquivo)
    
respostasCorretas = ["1-A","2-C","3-B","4-D","5-A","6-D","7-E","8-A","9-C","10-E"]

imagem = cv2.imread('imagem.jpeg')


if imagem is None:
    print("Falha ao carregar a imagem")
else:
    imagem = cv2.resize(imagem,(600,700))
    gabarito,bbox = exG.extrairMaiorCtn(imagem)
    imgGray = cv2.cvtColor(gabarito, cv2.COLOR_BGR2GRAY)
    ret,imgTh = cv2.threshold(imgGray,70,255,cv2.THRESH_BINARY_INV)
    cv2.rectangle(imagem, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (0, 255,0), 3)
    respostas = []
    for id,vg in enumerate(campos):
        x = int(vg[0])
        y = int(vg[1])
        w = int(vg[2])
        h = int(vg[3])
        cv2.rectangle(gabarito, (x, y), (x + w, y + h),(0,0,255),2)
        cv2.rectangle(imgTh, (x, y), (x + w, y + h), (255, 255, 255), 1)
        campo = imgTh[y:y + h, x:x + w]
        height, width = campo.shape[:2]
        tamanho = height * width
        pretos = cv2.countNonZero(campo)
        percentual = round((pretos / tamanho) * 100, 2)
        if percentual >=15:
            cv2.rectangle(gabarito, (x, y), (x + w, y + h), (255, 0, 0), 2)
            respostas.append(resp[id])

    #print(respostas)
    erros = 0
    acertos = 0
    if len(respostas)==len(respostasCorretas):
        for num,res in enumerate(respostas):
            if res == respostasCorretas[num]:
                acertos +=1
            else:
                erros +=1

        cv2.putText(imagem,f'ACERTOS: {acertos}',(30,140),cv2.FONT_HERSHEY_SIMPLEX,1.2,(0,0,255),3)

    cv2.imshow('img',imagem)
    cv2.imshow('Gabarito', gabarito)
    cv2.imshow('IMG TH', imgTh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
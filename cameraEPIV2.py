import cv2
import boto3
import numpy as np
import os

# Define as credenciais da AWS
access_key_id = '(coloque sua chave)'
secret_access_key = '(coloque sua chave de acesso)'

# Define o nome da pasta onde as imagens serão salvas
image_folder = 'epi_images'

# Verifica se a pasta existe e cria se não existir
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# Define a função para detectar EPI usando o Amazon Rekognition
def detectar_EPI(frame):
    rekognition = boto3.client('rekognition', 
                               region_name='us-east-1', 
                               aws_access_key_id=access_key_id, 
                               aws_secret_access_key=secret_access_key)
    _, img_encoded = cv2.imencode('.jpg', frame)
    img_bytes = img_encoded.tobytes()
    response = rekognition.detect_protective_equipment(
        Image={
            'Bytes': img_bytes
        },
        SummarizationAttributes={
            'MinConfidence': 90,
            'RequiredEquipmentTypes': ['FACE_COVER', 'HAND_COVER']
        }
    )
    for person in response['Persons']:
        if person['BodyParts'][0]['EquipmentDetections']:
            return True
    return False

# Captura a partir da câmera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if ret:
        # O frame foi lido com sucesso, você pode prosseguir com o processamento
        # ...

        # Detecta humanos na imagem
        body_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        bodies = body_classifier.detectMultiScale(gray, 1.1, 3)

        # Verifica se cada pessoa detectada está usando EPI
        for (x, y, w, h) in bodies:
            roi = frame[y:y + h, x:x + w]
            has_EPI = detectar_EPI(roi)
            if not has_EPI:
                # Salva a imagem sem EPI na pasta
                img_name = os.path.join(image_folder, f'epi_{len(os.listdir(image_folder)) + 1}.jpg')
                cv2.imwrite(img_name, roi)

            # Desenha um retângulo ao redor da pessoa na imagem
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, 'Humano', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

        # Exibe a imagem capturada
        cv2.imshow('Camera', frame)

    if cv2.waitKey(1) == ord('q'):
        break

# Libera a câmera e fecha as janelas
cap.release()
cv2.destroyAllWindows()
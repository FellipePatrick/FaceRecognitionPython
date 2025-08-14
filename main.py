import cv2
import os
from deepface import DeepFace
import numpy as np

# Pasta com subpastas de cada pessoa
db_path = "./fotos_cadastradas"

# Pré-calcula embeddings do banco
print("Pré-calculando embeddings do banco de rostos...")
embeddings_db = {}
for person_name in os.listdir(db_path):
    person_folder = os.path.join(db_path, person_name)
    if os.path.isdir(person_folder):
        embeddings_db[person_name] = []
        for img_file in os.listdir(person_folder):
            if img_file.endswith(('.jpg', '.png')):
                img_path = os.path.join(person_folder, img_file)
                embedding = DeepFace.represent(img_path, enforce_detection=False)[0]["embedding"]
                embeddings_db[person_name].append(np.array(embedding))

print("Embeddings calculados!")

# Inicializa webcam
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(80,80))

    for (x, y, w, h) in faces:
        face_crop = frame[y:y+h, x:x+w]

        try:
            # Calcula embedding do rosto detectado
            face_embedding = np.array(DeepFace.represent(face_crop, enforce_detection=False)[0]["embedding"])
            
            # Compara com todos os embeddings do banco
            name = "Desconhecido"
            min_distance = float("inf")
            threshold = 0.6  # Limite de similaridade, pode ajustar

            for person_name, person_embeddings in embeddings_db.items():
                for db_emb in person_embeddings:
                    dist = np.linalg.norm(face_embedding - db_emb)
                    if dist < min_distance:
                        min_distance = dist
                        if dist < threshold:
                            name = person_name
                        else:
                            name = "Desconhecido"

        except:
            name = "Desconhecido"

        # Desenha retângulo e nome
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

    cv2.imshow("Reconhecimento Facial Rápido", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

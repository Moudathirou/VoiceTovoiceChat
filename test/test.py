import cv2
import numpy as np
import dlib
from scipy.io import wavfile

# Charger l'image
image_path = 'C:/Users/ips17101/Desktop/auto_rag/rf.png'
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Charger le détecteur de visage
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# Détection de visage
faces = detector(gray)
if len(faces) == 0:
    raise Exception("Aucun visage détecté dans l'image")

# Prendre le premier visage détecté
face = faces[0]

# Obtenir les points de repère du visage
landmarks = predictor(gray, face)
landmarks_points = []
for n in range(48, 68):
    x = landmarks.part(n).x
    y = landmarks.part(n).y
    landmarks_points.append((x, y))

# Charger l'audio
audio_path = 'output.wav'
sample_rate, audio_data = wavfile.read(audio_path)

# Normaliser les données audio
audio_data = audio_data / np.max(np.abs(audio_data))

# Simulation de mouvement de lèvres basé sur l'amplitude audio
# Note: Pour une synchronisation précise, une analyse plus complexe est nécessaire
for frame in range(len(audio_data)):
    lip_movement = audio_data[frame] * 20  # Ajuster le multiplicateur selon les besoins
    for i in range(48, 68):
        cv2.circle(image, landmarks_points[i], int(lip_movement), (0, 0, 255), -1)
    
    # Sauvegarder ou afficher le cadre
    cv2.imwrite(f'frame_{frame}.jpg', image)
    # cv2.imshow('Lip Sync', image)
    # cv2.waitKey(1)

# Nettoyer
cv2.destroyAllWindows()

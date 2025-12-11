import cv2
from modules.config import FULLBODY_CASCADE_PATH, CAR_CASCADE_PATH

class Detector:
    def __init__(self):
        self.body_cascade = cv2.CascadeClassifier()
        self.car_cascade = cv2.CascadeClassifier()
        
        if not self.body_cascade.load(FULLBODY_CASCADE_PATH):
            raise IOError(f"Error loading {FULLBODY_CASCADE_PATH}")
        if not self.car_cascade.load(CAR_CASCADE_PATH):
            raise IOError(f"Error loading {CAR_CASCADE_PATH}")

    def detect_people(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        bodies = self.body_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in bodies:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return len(bodies)

    def detect_cars(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cars = self.car_cascade.detectMultiScale(gray, 1.1, 1)
        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        return len(cars)

            ###############################################################################
            #                              CLASE DETECTOR                                 #
            #-----------------------------------------------------------------------------#
            # FUNCIÓN: Implementa detección básica de objetos (personas y vehículos)      #
            #          utilizando clasificadores Haar Cascade de OpenCV.                  #
            #                                                                             #
            # ELEMENTOS CLAVE:                                                            #
            #   1. __init__: Carga los modelos pre-entrenados (XML) para su uso.          #
            #   2. detect_people: Detecta cuerpos completos, dibuja rectángulos AZULES    #
            #      y devuelve el conteo.                                                  #
            #   3. detect_cars: Detecta vehículos, dibuja rectángulos ROJOS y devuelve    #
            #      el conteo.                                                             #
            #                                                                             #
            # FLUJO SIMPLIFICADO: FRAME -> (Convertir a escala de grises) ->              #
            #                     (Aplicar Cascade.detectMultiScale) ->                   #
            #                     (Dibujar + Contar) -> Devolver Conteo                   #
            ###############################################################################

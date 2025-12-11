import csv
import os
from datetime import datetime
from modules.config import DATA_FILE_PATH

def save_data(people_count, car_count):
    file_exists = os.path.isfile(DATA_FILE_PATH)
    with open(DATA_FILE_PATH, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Timestamp', 'Personas', 'Autos'])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), people_count, car_count])



        #############################################################
        #                    FUNCIÓN save_data                      #
        #-----------------------------------------------------------#
        # FUNCIÓN: Guarda datos básicos de conteo (personas y       #
        #          vehículos) en un archivo CSV.                    #
        #                                                           #
        # OPERACIONES ELEMENTALES:                                  #
        #   1. Verifica si el archivo de datos ya existe.           #
        #   2. Si no existe, crea el archivo y escribe los          #
        #      encabezados de columna.                              #
        #   3. Agrega una nueva fila con:                           #
        #      - Fecha y hora actual                                #
        #      - Conteo de personas                                 #
        #      - Conteo de vehículos                                #
        #                                                           #
        # FLUJO: VERIFICAR ARCHIVO -> (ESCRIBIR ENCABEZADOS si es   #
        #        nuevo) -> AGREGAR FILA DE DATOS                    #
        #############################################################   
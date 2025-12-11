import cv2
import time
from modules.config import ROJO, VERDE, VIDEO_PATH
from modules.detectors import Detector
from modules.data_manager import save_data

def main():
    try:
        detector = Detector()
    except IOError as e:
        print(e)
        return

    cap = cv2.VideoCapture(VIDEO_PATH)

    if not cap.isOpened():
        print(f"Error opening video: {VIDEO_PATH}")
        return

    traffic_light_state = ROJO
    green_start_time = 0
    last_person_check_time = time.time()
    last_save_time = time.time()
    
    last_printed_state = ""
    last_people_count = 0
    last_car_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        people_count = detector.detect_people(frame)
        car_count = detector.detect_cars(frame)
        
        current_time = time.time()

        if current_time - last_save_time >= 1.0:
            save_data(people_count, car_count)
            last_save_time = current_time

        if traffic_light_state == ROJO:
            if current_time - last_person_check_time >= 30:
                if people_count > 0:
                    traffic_light_state = VERDE
                    green_start_time = time.time()
                last_person_check_time = current_time
        elif traffic_light_state == VERDE:
            elapsed_green = current_time - green_start_time
            remaining_green = 15 - int(elapsed_green)
            if remaining_green <= 0:
                traffic_light_state = ROJO
        
        if traffic_light_state == ROJO:
            if last_printed_state != ROJO or people_count != last_people_count or car_count != last_car_count:
                print(f"State: {traffic_light_state}, People: {people_count}, Cars: {car_count}")
                last_printed_state = ROJO
                last_people_count = people_count
                last_car_count = car_count
        else:
            elapsed_green = current_time - green_start_time
            remaining_green = 15 - int(elapsed_green)
            if last_printed_state != VERDE or people_count != last_people_count or car_count != last_car_count or remaining_green % 5 == 0:
                 print(f"State: {traffic_light_state}, Green Time Left: {remaining_green}s, People: {people_count}, Cars: {car_count}")
                 last_printed_state = VERDE
                 last_people_count = people_count
                 last_car_count = car_count

        cv2.imshow("Smart Traffic Light", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

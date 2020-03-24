import cv2
import os

root_path = os.path.abspath(".")

def get_classes():
    classes_list = os.listdir(ospath.path.join(root_path,"samples"))
    return classes_list

# def get_defect_xml():
#     classes_list = get_classes()
#     for c in classes_list:
#         item = cv2.Cascadeclassifier("cascade.xml")
#         item.load

# def detect_thing(img,class_name):
#     detector = cv2.Cascadeclassifier("cascade.xml")
#     detected_things = detector.load(os.path.join(root_path,"training_set",class_name,"cascade.xml"))


if __name__ == "__main__":
    class_name="magic_cube"
    # detector = cv2.CascadeClassifier("cascade.xml")
    print(os.path.join(root_path,"training_set",class_name,"cascade.xml"))
    detector = cv2.CascadeClassifier(os.path.join(root_path,"training_set",class_name,"cascade.xml"))
    # detector.load(os.path.join(root_path,"training_set",class_name,"cascade.xml"))

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        # rect = 0
        rect = detector.detectMultiScale(frame)
        for (x, y, w, h) in rect:  
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) 
        print(rect)
        print(1)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
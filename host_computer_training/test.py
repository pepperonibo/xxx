import cv2
import os

root_path = os.path.abspath(".")

if __name__ == "__main__":
    class_name="magic_cube"
    # detector = cv2.CascadeClassifier("cascade.xml")
    print(os.path.join(root_path,"training_set",class_name,"cascade.xml"))
    detector = cv2.CascadeClassifier('cascade.xml')
    # detector.load(os.path.join(root_path,"training_set",class_name,"cascade.xml"))

    img = cv2.imread("./1.jpg")
    rects = detector.detectMultiScale(img, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
    if len(rects): # 大于0则检测到人脸
        for rect in rects: # 单独框出每一张人脸
            x, y, w, h = rect
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            print(rect)
    cv2.imshow("image", img) # 显示图像
    c = cv2.waitKey(10)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
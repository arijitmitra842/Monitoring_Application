import cv2
import winsound
camera = cv2.VideoCapture(0)
while camera.isOpened():
    ret, frame_01 = camera.read()
    ret, frame_02 = camera.read()
    difference = cv2.absdiff(frame_01, frame_02)
    gray_color = cv2.cvtColor(difference, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray_color, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations = 4)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for i in contours:
        if cv2.contourArea(i) < 6000:
            continue
        x, y, w, h = cv2.boundingRect(i)
        cv2.rectangle(frame_01, (x, y), (x+w, y+h), (0, 255, 0), 3)
        winsound.PlaySound("alert_sound.wav", winsound.SND_ASYNC)
    if cv2.waitKey(15) == ord("a"):
        break
    cv2.imshow("Virtual Camera", frame_01)

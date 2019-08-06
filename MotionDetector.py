import cv2, time, numpy


if __name__ == '__main__':
    first_frame = None
    current_frame = None
    video = cv2.VideoCapture(0)

    a = 1


    while True:
        a = +1
        check,frame = video.read()
        print(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21,21), 0)

        if first_frame is None:
            first_frame = gray
            current_frame = gray
            continue

        delta_frame = cv2.absdiff(current_frame, gray)
        thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
        thresh_delta = cv2.dilate(thresh_delta, None, iterations=0)
        (_,cnts,_) = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in cnts:
            if cv2.contourArea(contour) < 1000:
                continue
            (x,y,w,h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)

        current_frame = gray
        cv2.imshow('frame', frame)
        cv2.imshow("capture", gray)
        cv2.imshow('delta', delta_frame)
        cv2.imshow('thresh', thresh_delta)
        key = cv2.waitKey(1)
        if key == ord('e'):
            break
    video.release()
    cv2.destroyAllWindows()
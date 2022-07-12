import cv2


def write_video(window_name, camera_id, fps):
    cap = cv2.VideoCapture(camera_id)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    h = int(cap.get(3))
    w = int(cap.get(4))
    vw = cv2.VideoWriter(r'D:\CV_test\out_video\video.mp4', fourcc, fps, (h, w))
    while cap.isOpened():
        flag, frame = cap.read()
        if not flag:
            break
        vw.write(frame)
        cv2.imshow(window_name, frame)
        if cv2.waitKey(1000//fps) & 0xFF == ord('q'):
            break
    cap.release()
    vw.release()
    cv2.destroyAllWindows()


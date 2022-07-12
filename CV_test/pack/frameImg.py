import cv2


def frame_write(PATH, image_name):
    cap = cv2.VideoCapture(PATH)
    frame_count = 0
    while cap.isOpened():
        flag, frame = cap.read()
        if not flag:
            break
        save_path = r'D:\CV_test\images\{}_{}.jpg'.format(image_name, frame_count)
        cv2.imwrite(save_path, frame)
        frame_count += 1
    cap.release()
    print('写入结束')


if __name__ == "__main__":
    frame_write(r'D:\CV_test\out_video\video_new.mp4', "test")
    print(111)

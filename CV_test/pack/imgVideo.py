import cv2


def img_video(file_name, fps):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    imgInfo = cv2.imread('D:\CV_test\images\{}_0.jpg'.format(file_name)).shape
    size = (imgInfo[1], imgInfo[0])
    vw = cv2.VideoWriter(r'D:\CV_test\out_video\video_new.mp4', fourcc, fps, size)
    file_count = 0
    while True:
        img = cv2.imread('D:\CV_test\images\{}_{}.jpg'.format(file_name, file_count))
        if img is None:
            print('end')
            break
        print(file_count)
        vw.write(img)
        file_count += 1
    vw.release()

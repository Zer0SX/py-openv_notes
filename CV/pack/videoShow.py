import cv2


def catchUsbVideo(window_name, camera_idx):
    cv2.namedWindow(window_name)  # 写入打开时视频框的名称
    # 捕捉摄像头
    cap = cv2.VideoCapture(camera_idx)  # camera_idx 的参数是0代表是打开笔记本的内置摄像头，也可以写上自己录制的视频路径
    while cap.isOpened():  # 判断摄像头是否打开，打开的话就是返回的是True
        # 读取图像
        # 读取一帧图像，该方法返回两个参数，flag: true 成功 false失败，frame:一帧的图像，是个三维矩阵，当输入的是一个是视频文件，读完flag==false
        flag, frame = cap.read()
        if not flag:  # 如果读取帧数不是正确的则ok就是False则该语句就会执行
            break

        # 显示图像
        cv2.imshow(window_name, frame)  # 显示视频到窗口
        key = cv2.waitKey(10)  # 30帧一帧图像间隔1000/30 ms
        if key & 0xFF == ord('q') or key & 0xFF == ord('Q'):  # 键盘按q/Q退出视频
            break

    cap.release()  # 释放摄像头
    cv2.destroyAllWindows()  # 销毁所有窗口


if __name__ == "__main__":
    try:
        catchUsbVideo('Camera', 0)
    except:
        print("error")
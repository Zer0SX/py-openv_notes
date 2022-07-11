import cv2


def writeVideo(window_name, camera_idx):
    cap = cv2.VideoCapture(camera_idx)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 代表解包，等同于'm','p','4','v'
    # 30表示帧率，(680,480)表示分辨率
    vm = cv2.VideoWriter('../out_video/output.mp4', fourcc, 30, (680, 480))
    while cap.isOpened():
        flag, frame = cap.read()
        if not flag:
            print('can not read frame, Exiting')
            break
        vm.write(frame)  # 写入每一帧
        cv2.imshow(window_name, frame)  # 窗口展示每一帧
        if cv2.waitKey(33) & 0xFF == ord('q'):  # 键盘按q退出视频
            break
    cap.release()  # 释放摄像头
    vm.release()  # 释放写入
    cv2.destroyAllWindows()  # 销毁窗口


if __name__ == "__main__":
    try:
        writeVideo('Camera Write', 0)
    except:
        print("error")

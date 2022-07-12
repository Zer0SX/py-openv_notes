from pack import videoWrite
from pack import frameImg
from pack import imgVideo


if __name__ == '__main__':
    videoWrite.write_video('camera', 0, 25)
    frameImg.frame_write(r'D:\CV_test\out_video\video.mp4', 'test')
    imgVideo.img_video('test', 30)
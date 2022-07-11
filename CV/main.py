import cv2
from pack import imgShow  # 图片展示
from pack import videoShow  # 视频抓取
from pack import videoWrite  # 视频录制

# ******************************************读取文件**************************************************
image = cv2.imread('./images/cat1.jpg')  # 读取图片文件
imgShow.img_show('Cat', image)  # 调用图片展示函数
# ******************************************视频抓取**************************************************
videoShow.catchUsbVideo('Camera', 0)
# ******************************************视频录制**************************************************
videoWrite.writeVideo('Camera Write', 0)

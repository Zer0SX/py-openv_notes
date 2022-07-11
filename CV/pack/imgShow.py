import cv2


# 封装图片展示函数
def img_show(name, img):
    cv2.namedWindow(name)  # 创建窗口
    # 展示图片，
    # 由于opencv读取图片数据的通道不是默认RGB而是BGR，颜色会发生改变，不要用别的库方式去展示
    cv2.imshow(name, img)

    # 等待按键
    # waitKey会返回ASCII码的值，
    # 其他整数表示等待按键的时间（ms），可以利用waitKey来销毁窗口
    while True:
        cap_key = cv2.waitKey(0)  # 接收键盘输入的ASCII码
        if cap_key & 0xFF == ord('q') or cap_key & 0xFF == ord('Q'):  # 判断，注：ord表示取ASCII码,int16位,ASCII8位，使用&
            break
        elif cap_key & 0xFF == ord('s') or cap_key & 0xFF == ord('S'):
            cv2.imwrite('../out_images/1.jpg', img)
            print('successful save')
    cv2.destroyAllWindows()  # 销毁窗口


if __name__ == "__main__":
    try:
        image = cv2.imread('../images/cat1.jpg')  # 读取图片文件
        img_show('Cat', image)  # 调用图片展示函数
    except:
        print("error")


from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
import mypage
import cv2

from functools import partial
from ImageSteganography_LSB import ImageSteganography
from ImageSteganography_DCT import DCT_Embed
import ImageSteganography_DWT
from TextSteganography_LSB import TextSteganography
from PIL import Image
from pylab import *



def HideInformation(ui):
    inputpath = ui.lineEdit.text()
    message = ui.textEdit.toPlainText()
    outputpath = ui.lineEdit_2.text()

    if inputpath == '' or message == '' or outputpath == '':
        ui.label_26.setPixmap(QPixmap(""))
        ui.tip1()
    else:
        TextSteganography.encode(inputpath, outputpath, message)
        ui.showimage3()
        ui.success1()
                

def ExtractInformation(ui):
    img = ui.lineEdit_3.text()
    if img == '':
        ui.textEdit_2.setText('')
        ui.tip1()
    else:
        result = TextSteganography.decode(img)
        if (result == 0):                           #
            ui.textEdit_2.setText('')
            ui.warn4()
        else:
            ui.textEdit_2.setText(str(result))
            ui.success2()


def HideImage(ui):
    image1 = ui.lineEdit_7.text()
    image2 = ui.lineEdit_8.text()
    outputpath1 = ui.lineEdit_10.text()
    if image1 == '' or image2 == '' or outputpath1 == '':
        ui.label_29.setPixmap(QPixmap(""))
        ui.tip1()
    else:


        if ui.comboBox_3.currentText() == 'DCT':

            root = ".."
            alpha = 100
            blocksize = 8
            watermark = cv2.imread(image2.format(root), cv2.IMREAD_GRAYSCALE)
            watermark = np.where(watermark < np.mean(watermark), 0, 1)
            background = cv2.imread(image1.format(root))
            background = cv2.cvtColor(background, cv2.COLOR_BGR2RGB)
            yuv_background = cv2.cvtColor(background, cv2.COLOR_RGB2YUV)
            Y, U, V = yuv_background[..., 0], yuv_background[..., 1], yuv_background[..., 2]
            bk = U


            dct_emb = DCT_Embed(block_size=blocksize, alpha=alpha)

            if not (ui.tip5(bk, watermark)):

                background_dct_blocks = dct_emb.dct_blkproc(background=bk)

                embed_watermak_blocks = dct_emb.dct_embed(dct_data=background_dct_blocks,
                                                          watermark=watermark)

                synthesis = dct_emb.idct_embed(dct_data=embed_watermak_blocks)
                yuv_background[..., 1] = synthesis
                rbg_synthesis = cv2.cvtColor(yuv_background, cv2.COLOR_YUV2RGB)

                image_pil = Image.fromarray(rbg_synthesis)
                image_pil.save(outputpath1)
                ui.showimage1()
                ui.tip2()

        elif ui.comboBox_3.currentText() == 'DWT':

            waterImg = cv2.imread(image2)
            Img = cv2.imread(image1)
            newImage = ImageSteganography_DWT.setwaterMark(waterImg, Img, 10)
            image_pil = Image.fromarray(newImage)
            image_pil.save(outputpath1)
            ui.showimage1()
            ui.tip2()


        elif ui.comboBox_3.currentText() == 'LSB':
            merged_image = ImageSteganography.merge(Image.open(image1), Image.open(image2))
            if merged_image == 0:
                ui.tip4()
            else:
                merged_image.save(outputpath1)
                ui.showimage1()
                ui.tip2()




def ExtractImage(ui):
    image3 = ui.lineEdit_11.text()
    outputpath2 = ui.lineEdit_13.text()
    image4 = ui.lineEdit_14.text()
    if image3 == '' or outputpath2 == '':
        ui.label_31.setPixmap(QPixmap(""))
        ui.tip1()
    else:
        if ui.comboBox_4.currentText() == 'DCT':
            width = ui.lineEdit_20.text()
            height = ui.lineEdit_21.text()
            if width == '' or height == '':
                ui.tip1()
            else:
                root = ".."
                dct_emb = DCT_Embed(8, 100)

                image = cv2.imread(image3.format(root), cv2.IMREAD_GRAYSCALE)

                image_dct_blocks = dct_emb.dct_blkproc(background=image)
                synthesis2 = dct_emb.idct_embed(dct_data=image_dct_blocks)
                extract_watermark = dct_emb.dct_extract(synthesis=synthesis2, watermark_size=(int(width), int(height))) * 255

                extract_watermark.astype(np.uint8)

                image_pil = Image.fromarray(extract_watermark)
                if image_pil.mode == "F":
                    image_pil = image_pil.convert('L')
                image_pil.save(outputpath2)
                ui.showimage2()
                ui.tip3()


        elif ui.comboBox_4.currentText() == 'DWT':
            if image4 == '':
                ui.tip1()
            else:
                # DWT 提取
                # 读取原始图像、嵌入水印图像
                originalImage = cv2.imread(image4)
                Img = cv2.imread(image3)
                # 水印提取
                waterImg = ImageSteganography_DWT.getwaterMark(originalImage, Img, 10)
                image_pil = Image.fromarray(waterImg)
                image_pil.save(outputpath2)
                ui.showimage2()
                ui.tip3()


        elif ui.comboBox_4.currentText() == 'LSB':
            # LSB 提取
            unmerged_image = ImageSteganography.unmerge(Image.open(image3))  # 进行图片提取
            unmerged_image.save(outputpath2)
            ui.showimage2()
            ui.tip3()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = mypage.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # 文本信息隐藏按钮
    ui.pushButton_3.clicked.connect(partial(HideInformation, ui))
    # 文本信息提取按钮
    ui.pushButton_5.clicked.connect(partial(ExtractInformation, ui))
    # 图像里藏图像按钮
    ui.pushButton_15.clicked.connect(partial(HideImage, ui))
    # 提取图片中隐藏图像按钮
    ui.pushButton_19.clicked.connect(partial(ExtractImage, ui))
    
    sys.exit(app.exec_())

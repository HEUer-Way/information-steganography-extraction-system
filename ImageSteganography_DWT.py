

import cv2
import pywt
import numpy as np





def arnold(img, key):
    r = img.shape[0]
    c = img.shape[1]
    p = np.zeros((r, c), np.uint8)

    a = 1
    b = 1
    for k in range(key):
        for i in range(r):
            for j in range(c):
                x = (i + b * j) % r
                y = (a * i + (a * b + 1) * j) % c
                p[x, y] = img[i, j]
    return p



def deArnold(img, key):
    r = img.shape[0]
    c = img.shape[1]
    p = np.zeros((r, c), np.uint8)

    a = 1
    b = 1
    for k in range(key):
        for i in range(r):
            for j in range(c):
                x = ((a * b + 1) * i - b * j) % r
                y = (-a * i + j) % c
                p[x, y] = img[i, j]
    return p


def setwaterMark(waterTmg, Img, key):
    print('水印嵌入...')
    Img = cv2.resize(Img, (400, 400))
    waterTmg = cv2.resize(waterTmg, (201, 201))


    Img1 = cv2.cvtColor(Img, cv2.COLOR_RGB2GRAY)
    waterTmg1 = cv2.cvtColor(waterTmg, cv2.COLOR_RGB2GRAY)


    waterTmg1 = arnold(waterTmg1, key)

    cv2.waitKey(0)

    c = pywt.wavedec2(Img1, 'db2', level=3)
    [cl, (cH3, cV3, cD3), (cH2, cV2, cD2), (cH1, cV1, cD1)] = c


    waterTmg1 = cv2.resize(waterTmg1, (101, 101))
    cv2.waitKey(0)
    d = pywt.wavedec2(waterTmg1, 'db2', level=1)
    [ca1, (ch1, cv1, cd1)] = d


    a1 = 0.1
    a2 = 0.2
    a3 = 0.1
    a4 = 0.1


    cl = cl + ca1 * a1
    cH3 = cH3 + ch1 * a2
    cV3 = cV3 + cv1 * a3
    cD3 = cD3 + cd1 * a4


    newImg = pywt.waverec2([cl, (cH3, cV3, cD3), (cH2, cV2, cD2), (cH1, cV1, cD1)], 'db2')
    newImg = np.array(newImg, np.uint8)
    newImg = cv2.cvtColor(newImg, cv2.COLOR_GRAY2RGB)
    return newImg



def getwaterMark(originalImage, Img, key):
    print('水印提取...')

    originalImage = cv2.resize(originalImage, (400, 400))

    Img1 = cv2.cvtColor(originalImage, cv2.COLOR_RGB2GRAY)
    Img = cv2.cvtColor(Img, cv2.COLOR_RGB2GRAY)

    cv2.waitKey(0)


    c = pywt.wavedec2(Img, 'db2', level=3)
    [cl, (cH3, cV3, cD3), (cH2, cV2, cD2), (cH1, cV1, cD1)] = c


    d = pywt.wavedec2(Img1, 'db2', level=3)
    [dl, (dH3, dV3, dD3), (dH2, dV2, dD2), (dH1, dV1, dD1)] = d


    a1 = 0.1
    a2 = 0.2
    a3 = 0.1
    a4 = 0.1


    ca1 = (cl - dl) * 10
    ch1 = (cH3 - dH3) * 5
    cv1 = (cV3 - dV3) * 10
    cd1 = (cD3 - dD3) * 10


    waterImg = pywt.waverec2([ca1, (ch1, cv1, cd1)], 'db2')
    waterImg = np.array(waterImg, np.uint8)

    cv2.waitKey(0)


    waterImg = deArnold(waterImg, key)
    return waterImg



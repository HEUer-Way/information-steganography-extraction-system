
#  -*- coding:utf-8 -*-


import cv2
import numpy as np

class DCT_Embed(object):
    def __init__(self, block_size=8, alpha=30):


        self.block_size = block_size

        self.alpha = alpha

        self.k1 = np.random.randn(block_size)
        self.k2 = np.random.randn(block_size)


    def dct_blkproc(self, background):

        background_dct_blocks_h = background.shape[0] // self.block_size
        background_dct_blocks_w = background.shape[1] // self.block_size
        background_dct_blocks = np.zeros(shape=(
            (background_dct_blocks_h, background_dct_blocks_w, self.block_size, self.block_size)
        ))


        h_data = np.vsplit(background, background_dct_blocks_h)
        for h in range(background_dct_blocks_h):
            block_data = np.hsplit(h_data[h], background_dct_blocks_w)
            for w in range(background_dct_blocks_w):
                a_block = block_data[w]
                background_dct_blocks[h, w, ...] = cv2.dct(a_block.astype(np.float64))  # dct变换
        return background_dct_blocks

    def dct_embed(self, dct_data, watermark):

        temp = watermark.flatten()
        assert temp.max() == 1 and temp.min() == 0, "为方便处理，请保证输入的watermark是被二值归一化的"

        result = dct_data.copy()
        for h in range(watermark.shape[0]):
            for w in range(watermark.shape[1]):
                k = self.k1 if watermark[h, w] == 1 else self.k2

                for i in range(self.block_size):
                    result[h, w, i, self.block_size - 1] = dct_data[h, w, i, self.block_size - 1] + self.alpha * k[i]
        return result

    def idct_embed(self, dct_data):

        row = None
        result = None
        h, w = dct_data.shape[0], dct_data.shape[1]
        for i in range(h):
            for j in range(w):
                block = cv2.idct(dct_data[i, j, ...])
                row = block if j == 0 else np.hstack((row, block))
            result = row if i == 0 else np.vstack((result, row))
        return result.astype(np.uint8)

    def dct_extract(self, synthesis, watermark_size):

        w_h, w_w = watermark_size
        recover_watermark = np.zeros(shape=watermark_size)
        synthesis_dct_blocks = self.dct_blkproc(background=synthesis)
        p = np.zeros(8)
        for h in range(w_h):
            for w in range(w_w):
                for k in range(self.block_size):
                    p[k] = synthesis_dct_blocks[h, w, k, self.block_size - 1]
                if corr2(p, self.k1) > corr2(p, self.k2):
                    recover_watermark[h, w] = 1
                else:
                    recover_watermark[h, w] = 0
        return recover_watermark



def mean2(x):
    y = np.sum(x) / np.size(x);
    return y


def corr2(a, b):

    a = a - mean2(a)
    b = b - mean2(b)
    r = (a * b).sum() / np.sqrt((a * a).sum() * (b * b).sum())
    return r


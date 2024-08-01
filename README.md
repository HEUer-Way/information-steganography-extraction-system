该系统采用 Python 实现算法，QT 界面展示。主要提供了文本与图像的隐写和提取功能。
用户可以根据需要，选择将隐秘文字隐藏于图片中，或者将秘密图片隐藏于图片中，以及秘密
信息提取。具体可以选择使用哪种算法进行隐写与提取，集成了 LSB（最小有效位替换）、
DCT（离散余弦变换）、DWT（离散小波变换）算法。该系统参加校内算法设计比赛并获奖。
1、隐写：用户根据需要选择隐写文本信息，或者隐写图像信息，并且另需提供一张图片为
宿主图片。点击“生成”按钮之后，根据弹窗提示，选择需要保存生成图像的位置。执行隐写操作
后，即可将秘密信息隐藏于宿主图片中。
2、提取：用户需要提供一张包含了以上算法加密后的图片，根据需要，选择相应的类型进行
秘密信息提取，点击“提取”按钮之后，根据弹窗提示，选择隐秘信息需要保存的位置

效果如下：
![image](https://github.com/HEUer-Way/information-steganography-extraction-system/blob/master/images/LSB%E6%96%87%E6%9C%AC%E5%8A%A0%E5%AF%86%E4%B8%8E%E6%8F%90%E5%8F%96.png)
![image](https://github.com/HEUer-Way/information-steganography-extraction-system/blob/master/images/LSB%E5%9B%BE%E5%83%8F%E5%8A%A0%E5%AF%86%E4%B8%8E%E6%8F%90%E5%8F%96.png)
![image](https://github.com/HEUer-Way/information-steganography-extraction-system/blob/master/images/DWT%E5%9B%BE%E5%83%8F%E5%8A%A0%E5%AF%86%E4%B8%8E%E6%8F%90%E5%8F%96.png)
![image](https://github.com/HEUer-Way/information-steganography-extraction-system/blob/master/images/DCT%E5%9B%BE%E5%83%8F%E5%8A%A0%E5%AF%86%E4%B8%8E%E6%8F%90%E5%8F%96.png)

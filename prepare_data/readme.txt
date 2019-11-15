对于人脸检测
iou>0.65, 正例， 标签1
0.4<iou<0.65, part，标签-1
iou<0.3 负例 标签 0
landmark 标签-2

正例和负例用于训练分类，正例和part训练bbox
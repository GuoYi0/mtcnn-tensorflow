##Description
复现mtcnn, a Joint Face Detection and Alignment using Multi-task Cascaded Convolutional Networks
参考代码来源[mtcnn-tensorflow](https://github.com/AITTSMD/MTCNN-Tensorflow)

##Preprequisites
下载数据集[wider face](http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/)用于人脸检测，数据集[Celeba](http://mmlab.ie.cuhk.edu.hk/archive/CNN_FacePoint.htm)用于landmark detection

## 训练集
1. 下载[wider face](http://mmlab.ie.cuhk.edu.hk/projects/WIDERFace/)的训练部分，解压，得到`WIDER_train`,放在data目录下，data目录与该工程目录同级。
2. 下载[landmark训练集](http://mmlab.ie.cuhk.edu.hk/archive/CNN_FacePoint.htm)，解压
3. 运行`prepare_data/gen_12net_data.py`，为**PNet** 生成一系列人脸检测的训练数据.
4. 运行`prepare_data/gen_landmark_aug_12.py`，为**PNet** 生成一系列landmark检测的训练数据.
5. 运行`gen_imglist_pnet.py`合并两个训练集
6. 运行`gen_PNet_tfrecords.py`来生为 **PNet** 生成tfrecord
7. 训练 **PNet**
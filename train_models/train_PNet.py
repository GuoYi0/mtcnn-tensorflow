# coding:utf-8
from train_models.mtcnn_model import P_Net
from train_models.train import train


def train_PNet(base_dir, prefix, end_epoch, display, lr, restore):
    """
    :param base_dir: '../../DATA/imglists/PNet'
    :param prefix:  '../ckpt/%s_model/PNet_landmark/PNet' % model_name
    :param end_epoch:
    :param display:
    :param lr:
    :return:
    """
    net_factory = P_Net
    train(net_factory, prefix, end_epoch, base_dir, display=display, base_lr=lr, restore=restore)


def main():
    # data path
    base_dir = '../../DATA/imglists/PNet'
    model_name = 'MTCNN'
    # model_path = '../data/%s_model/PNet/PNet' % model_name
    # with landmark
    model_path = '../ckpt/%s_model/PNet' % model_name
    restore = True
    prefix = model_path
    end_epoch = 30
    display = 100
    lr = 0.001
    train_PNet(base_dir, prefix, end_epoch, display, lr, restore)


if __name__ == '__main__':
    main()

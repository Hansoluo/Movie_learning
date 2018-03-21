# Windows7 环境下配置 深度学习环境

之前一直在docker上面使用tensorflow，因为要在本地处理大量图片，因此在本地配置深度学习环境，没想到遇坑连连，记录之。

## 环境
- Windows 7.1 旗舰版 64位
- CPU：i3 M370@2.4GHz

## 安装TensorFlow CPU版本

- 必读[官方文档](https://www.tensorflow.org/install/install_windows#CommonInstallationProblems)

- 坑1：需要python3.5.x 64位版本
    + anaconda上使用的是python3.6版本,需要覆盖掉
    + 本地下载[python3.5.x 64位版本](https://www.python.org/downloads/release/python-352/)
    + 环境变量%PATH%重新覆盖为python 3.5
    + CLI下测试python版本，出现Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32字样

- 坑2：使用pip安装tensorflow，多次崩溃
    + 原因：国外源，下载慢
    + 解决：使用国内源 pip install tensorflow -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn

- 坑3：安装成功后导入报错
    + 报错：ImportError: No module named '_pywrap_tensorflow_internal'
    + 解决：安装Visual C++ 2015 redistributable
    + 参考：[ImportError](https://www.youtube.com/watch?v=Zgw--A7tOk4)

- 坑4：运行再次报错ImportError
    + 原因：电脑是旧的CPU，不支持AVX指令集
    + 解决：装回1.5版本的tensorflow
    + 命令：pip install tensorflow==1.5 -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn
    + 参考：[win10上安装tensorflow注意事项](http://blog.csdn.net/bianjun1075/article/details/60478487)

## 安装Keras

- 坑：同样下载速度慢
- 解决：使用国内源 pip install keras -U --pre -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn
- [keras官方文档](https://keras-cn.readthedocs.io/en/latest/for_beginners/keras_windows/)

## 安装Opencv3

- [使用Anaconda安装Opencv3](https://github.com/twtrubiks/FaceDetect/tree/master/How%20Easy%20Install%20OpenCV%20%20for%20Python%20use%20Anaconda)





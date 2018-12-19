# Windows7 环境下配置 深度学习环境

- 20180320：之前一直在docker上面使用tensorflow，因为要在本地处理大量图片，因此在本地配置深度学习环境，没想到遇坑连连，记录之。
- 20180321：本地python完成深度环境安装，anaconda未能成功
- 20180322：使用docker成功安装keras和OpenCV，仍然使用docker进行深度学习
- 20180326: 完成基于jypyter notebook 本地Windows 7的深度环境配置

## 环境
- Windows 7.1 旗舰版 64位
- CPU：i3 M370@2.4GHz

## 本地使用pip安装TensorFlow CPU版本

- 必读[官方文档](https://www.tensorflow.org/install/install_windows#CommonInstallationProblems)

- 坑1：需要python3.5.x 64位版本
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

## 本地使用Anaconda安装TensorFlow CPU版本
- 启动栏内的Anaconda Navigation 点击后闪退
- 通过在cmd中输入命令进入Anaconda Navigation界面
- Home界面中选择tensorflow环境，发现没有按照jupyter notebook
- 更新Anaconda Navigation版本
- 进入tensorflow环境内，完成jupyter notebook的安装
- 安裝好之後再點擊tensorflow的三角箭頭，就會看到open with spyder 和open with jupyter notebook，直接點擊就能進入了
- 安装好之后，启动栏出现jupyter notebook(tensorflow)快捷方式
- 右击属性可以对其启动路径进行配置
- 该环境内缺少的安装包可以通过Anaconda Navigation界面安装
- 参考资料
    + [通过 Anaconda 在 Jupyter 里运行 Tensorflow 及可视化](https://hacpai.com/article/1496391186149)
    + [win7 使用anaconda安裝tensorflow並且在jupyter notebook上啟動](https://hk.saowen.com/a/5acf1b92e41cb57e4a297dee186b44d4edefd2209649e521afddcebe950810a9)


## 安装Keras

- 坑：同样下载速度慢
- 解决：使用国内源 pip install keras -U --pre -i http://pypi.mirrors.ustc.edu.cn/simple --trusted-host pypi.mirrors.ustc.edu.cn
- [keras官方文档](https://keras-cn.readthedocs.io/en/latest/for_beginners/keras_windows/)


## 安装Opencv3

- [使用Anaconda安装Opencv3](https://github.com/twtrubiks/FaceDetect/tree/master/How%20Easy%20Install%20OpenCV%20%20for%20Python%20use%20Anaconda)
- 使用pip安装：pip install opencv-python
- 使用docker中的jupyter notebook安装
    + pip install opencv-python
    + [报错信息及处理](http://blog.csdn.net/yuanlulu/article/details/79017116)
- 验证：输入 import cv2，无报错信息即可






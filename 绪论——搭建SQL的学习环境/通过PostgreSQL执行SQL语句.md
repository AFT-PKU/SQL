# 《SQL基础教程》第2版读书笔记

## 前言

&emsp;&emsp;本书是畅销书《SQL基础教程》第2版，介绍了关系数据库以及用来操作关系数据库的SQL语言的使用方法。书中通过丰富的图示、大量示例程序和详实的操作步骤说明，让读者循序渐进地掌握SQL的基础知识和使用技巧，切实提高编程能力。每章结尾设置有练习题，帮助读者检验对各章内容的理解程度。另外，本书还将重要知识点总结为“法则”，方便读者随时查阅。第2版除了将示例程序更新为对应新版本的DB的SQL之外，还新增了一章，介绍如何从应用程序执行SQL。

&emsp;&emsp;这个项目记录了北京大学AFT协会对《SQL基础教程》第2版的学习笔记，同时也特别感谢Master_lisa为本书录制的[学习视频](https://www.bilibili.com/video/av62315714)


>GitHub的markdown不再支持tex公式的解析显示，使用Chrome的同学可以安装[GitHub with MathJax](https://chrome.google.com/webstore/detail/github-with-mathjax/ioemnmodlmafdkllaclgeombjnmnbima)添加MathJax的解析以对公式正常显示。

>如果需要直接阅读模式，可以移步至我们的github.io进行阅读：[《SQL基础教程》第2版读书笔记]()

## 目录

1. [数学基础](数学基础/README.md)
    1. [线性代数](数学基础/线性代数.md)
    1. [概率与信息论](数学基础/概率与信息论.md)
    1. [数值计算](数学基础/数值计算.md)
1. [机器学习基础与实践](机器学习基础与实践/README.md)
    1. [机器学习基础](机器学习基础与实践/机器学习基础.md)
    1. [TensorFlow实战](机器学习基础与实践/TensorFlow实战.md)
1. [深度前馈网络](深度前馈网络/README.md)
1. [深度学习中的正则化](深度学习中的正则化/README.md)
1. [深度学习中的优化](深度学习中的优化/README.md)
1. [卷积网络](卷积网络/README.md)
    1. [简单卷积网络示例](卷积网络/简单卷积网络.md)
    1. [经典CNN模型(LeNet and AlexNet)](卷积网络/卷积网络进阶.ipynb)
    1. [GoogLeNet](卷积网络/GoogLeNet.ipynb)
    1. [ResNet](卷积网络/ResNet.ipynb)
1. [循环递归网络](循环递归网络/README.md)
    1. [RNN示例](循环递归网络/RNN.md)
    1. [LSTM](循环递归网络/LSTM.md)
    1. [基于CharRNN的古诗生成](循环递归网络/poetry-charRNN.ipynb)
        <!-- 1. [序列到序列学习](循环递归网络/Sequence.md) -->
1. [实践调参](实践调参/README.md)
1. [线性因子模型](线性因子模型/README.md)
1. [自编码器](自编码器/README.md)
1. [表示学习](表示学习/README.md)
1. [结构化概率模型](结构化概率模型/README.md)
1. [蒙特卡洛方法](蒙特卡洛方法/README.md)
1. [玻尔兹曼机](玻尔兹曼机/README.md)
1. [有向生成网络](有向生成网络)
1. [生成对抗网络](生成对抗网络/README.md)

>持续更新中，欢迎贡献便于理解的优秀代码示例，推荐使用Python代码和Jupyter Notebook提交，并附上说明。

致谢
--------------------
我们分为两个类别的贡献者。
 - 负责人也就是对应的该章节案例维护者。
 - 贡献者对应于主要的案例开发者。

| 原书章节 | 对应案例  | 负责人 | 贡献者 |
| ------------ | ------------ | ------------ | ------------ |
| [第一章 前言](https://exacity.github.io/deeplearningbook-chinese/Chapter1_introduction/) | [前言介绍](README.md) | @swordyork | @daweicheng |
| [第二章 线性代数](https://exacity.github.io/deeplearningbook-chinese/Chapter2_linear_algebra/) | [线性代数](数学基础/线性代数.md) | @zengxy | |
| [第三章 概率与信息论](https://exacity.github.io/deeplearningbook-chinese/Chapter3_probability_and_information_theory/) | [概率与信息论](数学基础/概率与信息论.md) | @zengxy |  |
| [第四章 数值计算](https://exacity.github.io/deeplearningbook-chinese/Chapter4_numerical_computation/) | [数值计算](数学基础/数值计算.md) | @zengxy |  |
| [第五章 机器学习基础](https://exacity.github.io/deeplearningbook-chinese/Chapter5_machine_learning_basics/) |[机器学习基础与实践](机器学习基础与实践/README.md) |@zengxy  | @fangjie  |
| [第六章 深度前馈网络](https://exacity.github.io/deeplearningbook-chinese/Chapter6_deep_feedforward_networks/) | [深度前馈网络](深度前馈网络/README.md) | @kimliu0803 | @hjptriplebee @fangjie  |
| [第七章 深度学习中的正则化](https://exacity.github.io/deeplearningbook-chinese/Chapter7_regularization/) | [深度学习中的正则化](深度学习中的正则化/README.md) | @lupeng666 | @titicaca |
| [第八章 深度模型中的优化](https://exacity.github.io/deeplearningbook-chinese/Chapter8_optimization_for_training_deep_models/) | [深度学习中的优化](深度学习中的优化/README.md) | @jinshengwang92 | @lupeng666  |
| [第九章 卷积网络](https://exacity.github.io/deeplearningbook-chinese/Chapter9_convolutional_networks/) | [卷积网络](卷积网络/README.md) | @LiuCheng|  |
| [第十章 序列建模：循环和递归网络](https://exacity.github.io/deeplearningbook-chinese/Chapter10_sequence_modeling_rnn/) | [循环递归网络](循环递归网络/README.md) | @zengxy | @hjptriplebee |
| [第十一章 实践方法论](https://exacity.github.io/deeplearningbook-chinese/Chapter11_practical_methodology/) |[实践调参](实践调参/README.md)  | @daweicheng |  |
| [第十二章 应用](https://exacity.github.io/deeplearningbook-chinese/Chapter12_applications/) |  | |  |
| [第十三章 线性因子模型](https://exacity.github.io/deeplearningbook-chinese/Chapter13_linear_factor_models/) | [线性因子模型](线性因子模型/README.md) | @liqi | @YaoStriveCode |
| [第十四章 自编码器](https://exacity.github.io/deeplearningbook-chinese/Chapter14_autoencoders/) | [自编码器](自编码器/README.md) | @daweicheng |  |
| [第十五章 表示学习](https://exacity.github.io/deeplearningbook-chinese/Chapter15_representation_learning/) | [表示学习](表示学习/README.md) |@daweicheng  | |
| [第十六章 深度学习中的结构化概率模型](https://exacity.github.io/deeplearningbook-chinese/Chapter16_structured_probabilistic_modelling/) |[结构化概率模型](结构化概率模型/README.md) | @xuanming |
| [第十七章 蒙特卡罗方法](https://exacity.github.io/deeplearningbook-chinese/Chapter17_monte_carlo_methods/) | [蒙特卡洛方法](蒙特卡洛方法/README.md) | @xuanming |   |
| [第十八章 面对配分函数](https://exacity.github.io/deeplearningbook-chinese/Chapter18_confronting_the_partition_function/) |  | |  |
| [第十九章 近似推断](https://exacity.github.io/deeplearningbook-chinese/Chapter19_approximate_inference/) |  | | |
| [第二十章 深度生成模型](https://exacity.github.io/deeplearningbook-chinese/Chapter20_deep_generative_models/) |[玻尔兹曼机](玻尔兹曼机/README.md)<br> [有向生成网络](有向生成网络)<br> [生成对抗网络](生成对抗网络) | @vistep <br>@daweicheng<br>@swordyork | |
| 参考文献 | | |  |

还有很多同学提出了不少建议，我们都列在此处。

@CharlieSCC ...

如有遗漏，请务必通知我们，可以发邮件至`pkuscc@stu.pku.edu.cn`。
这是我们必须要感谢的，所以不要不好意思。

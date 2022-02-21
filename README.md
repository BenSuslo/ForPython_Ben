# name: SU
# time: 2022/2/17
# game: Alien invasion
# project: Armed spaceships
# describation:
    在游戏《外星人入侵》中，玩家控制着一艘最初出现在屏幕底部中央的飞船。玩家可以使用箭头键左右移动飞船，还可使用空格键进行射击。游戏开始时，一群外星人出现在天空中，他们在屏幕中向下移动。玩家的任务是射杀这些外星人。玩家将所有外星人都消灭干净后，将出现一群新的外星人，他们移动的速度更快。只要有外星人撞到了玩家的飞船或到达了屏幕底部，玩家就损失一艘飞船。玩家损失三艘飞船后，游戏结束。
# download Pygame:
    Pygame项目托管在代码分享网站Bitbucket中。要在Windows系统中安装Pygame，请访问https://bitbucket.org/pygame/pygame/downloads/，查找与你运行的Python版本匹配的Windows安装程序。如果在Bitbucket上找不到合适的安装程序，请去http://www.lfd.uci.edu/～gohlke/pythonlibs/#pygame看看。
    下载合适的文件后，如果它是.exe文件，就运行它。如果该文件的扩展名为.whl，就将它复制到你的项目文件夹中。再打开一个命令窗口，切换到该文件所在的文件夹，并使用pip来运行它：
    >python -m pip install --user pygame-1.9.2a0-cp35-none-win32.whl

Pygame 是 Pete Shinners 在 SDL（Simple DirectMedia Layer，一套开源的跨平台多媒体开发库）基础上开发而来，其目的是取代 PySDL。

通过 Pygame 我们能够创建各种各样的游戏和多媒体程序，但相比于开发大型 3D 游戏来说，它更擅长与开发 2D 游戏，比如扫雷、纸牌游戏、贪吃蛇、超级马里奥、飞机大战等，如果是 3D 游戏，可以选择一些功能更为全面的 Python 游戏开发库，比如 Panda3D（迪士尼开发的3D游戏引擎），PyOgre（Ogre 3D渲染引擎）等。

Pygame 的下载非常简单，可分为两种方式：一是通过 Python 的包管理器 pip 来安装；二是下载二进制安装包进行安装。其中使用 pip 包管理器安装是最简单、最轻量级的方法
1) pip包管理器安装
这是最为轻便的一种安装方式，推荐大家使用。首先确定的您的电脑已经安装了 Python（推荐使用 3.7 以上版本），然后打开 cmd 命令行工具，输入以下命令即可成功安装：
            pip install pygame
2) 二进制安装包安装
Python 第三方库官网 PyPI（点击前往下载）提供了不同操作平台的 Pygame 安装包
最后使用以下命令检查 Pygame 版本，从而验证是否安装成功。
python -m pygame --version

为游戏选择素材时，务必要注意许可。最安全、最不费钱的方式是使用http://pixabay.com/ 等网站提供的图形，这些图形无需许可，你可以对其进行修改。
在游戏中几乎可以使用任何类型的图像文件，但使用位图（.bmp）文件最为简单，因为Pygame默认加载位图。
就游戏《外星人入侵》而言，你可以使用文件ship.bmp（如图12-1所示），这个文件可在本书的配套资源（http://www.ituring.com.cn/book/1861）中找到。

<!-- 生成随机数 -->
from random import randint
random_number = randint(-10,10)
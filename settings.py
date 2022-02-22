# 每次给游戏添加新功能时，通常也将引入一些新设置。
# 下面来编写一个名为settings的模块，其中包含一个名为Settings的类，
# 用于将所有设置存储在一个地方，以免在代码中到处添加设置。
# 这样，我们就能传递一个设置对象，而不是众多不同的设置。
# 另外，这让函数调用更简单，且在项目增大时修改游戏的外观更容易：
# 要修改游戏，只需修改settings.py中的一些值，
# 而无需查找散布在文件中的不同设置。

class Settings():
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        # 在Pygame中，颜色是以RGB值指定的
        # 颜色值(255, 0, 0)表示红色，(0, 255, 0)表示绿色，而(0, 0, 255)表示蓝色。
        # 通过组合不同的RGB值，可创建1600万种颜色。
        self.bg_color = (230, 230, 230)
        # 飞船设置
        self.ship_limit = 3
        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # 外星人设置
        self.fleet_drop_speed = 10
        # 加快游戏节奏的速度
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
        # 计分
        self.alien_points = 50
    def increase_speed(self):
        """提高速度设置和外星人点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

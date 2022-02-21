import pygame
class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取其外接矩形
        # pygame.image.load()返回一个表示飞船的surface
        self.image = pygame.image.load('VSCode_for_Python\\alien_invasion\images\\rocket.png')
        #改变飞船大小
        self.image = pygame.transform.scale(self.image, (80, 120))
        # 使用get_rect()获取相应surface的属性rect
        #获取飞船外接矩形
        self.rect = self.image.get_rect()
        #获取屏幕外接矩形
        self.screen_rect = screen.get_rect()

        # 要将游戏元素居中，可设置相应rect对象的属性center、centerx或centery。
        # 要让游戏元素与屏幕边缘对齐，可使用属性top、bottom、left或right
        # 要调整游戏元素的水平或垂直位置，可使用属性x和y，它们分别是相应矩形左上角的x和y坐标
        # 在Pygame中，原点(0, 0)位于屏幕左上角，向右下方移动时，坐标值将增大。

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船的属性center中存储小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def update(self):
        """根据移动标志调整飞船位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
        # 根据self.center更新rect对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx
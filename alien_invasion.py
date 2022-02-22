import pygame
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
def run_game():
    """初始化游戏并创建一个屏幕对象"""
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    # 创建一个名为screen的显示窗口
    # 这个游戏的所有图形元素都将在其中绘制
    # 实参(1200, 800)是一个元组，指定了游戏窗口的尺寸，储存的是像素
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 对象screen是一个surface。
    # 在Pygame中，surface是屏幕的一部分，用于显示游戏元素。
    # 在这个游戏中，每个元素（如外星人或飞船）都是一个surface。
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    # 这个编组将是pygame.sprite.Group类的一个实例
    # pygame.sprite.Group类类似于列表，但提供了有助于开发游戏的额外功能
    bullets = Group()

    # 创建一个外星人编组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    """开始游戏的主循环"""
    while True:
        """监视键盘和鼠标事件"""
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        """让最近绘制的屏幕可见"""
        # pygame.display.flip()，命令Pygame让最近绘制的屏幕可见。
        pygame.display.flip()
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
run_game()

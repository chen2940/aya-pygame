import pygame

version = "V1.1"
SCREEN_WIDTH = 800  # 宽度
SCREEN_HEIGHT = 500  # 高度
BG_COLOR = pygame.Color(0, 0, 0)  # 颜色
TEXT_COLOR = pygame.Color(255, 0, 0)  # 字体颜色

window = None
my_tank = None
enemyTankList = []  # 敌方坦克列表
enemyTankCount = 5  # 敌方坦克数量
myBulletList = []  # 我方坦克子弹列表
enemyBulletList = []  # 敌方坦克子弹列表
explodeList = []  # 爆炸效果列表
WallList = []  # 墙壁列表

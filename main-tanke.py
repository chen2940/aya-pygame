import pygame, sys

_display = pygame.display
_font = pygame.font
COLOR_BLACK = pygame.Color(0, 0, 0)
COLOR_WRITE = pygame.Color(255, 255, 255)
version = "0.01 Bate"

class Tank():
    def __init__(self, left, top):
        self.images = {
            'U': pygame.image.load('img/p1tankU.gif'),
            'D': pygame.image.load('img/p1tankD.gif'),
            'L': pygame.image.load('img/p1tankL.gif'),
            'R': pygame.image.load('img/p1tankR.gif')
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        # 坦克所在的区域 Rect->
        self.rect = self.image.get_rect()
        self.rect.left = left
        # 指定坦克初始化位置 分别距 x，y 轴的位置
        self.rect.top = top

    # 展示坦克(将坦克这个 surface 绘制到窗口中 blit())
    def displayTank(self):
        # 1.重新设置坦克的图片
        self.image = self.images[self.direction]
        # 2.将坦克加入到窗口中
        MainGame.window.blit(self.image, self.rect)

class MainGame():
    # 游戏主窗口
    window = None
    SCREEN_HEIGHT = 768
    SCREEN_WIDTH = 1024

    def __init__(self):
        pass

    def getTextSurface(self, text):
        _font.init()
        font = _font.SysFont("kaiti", 18)
        textSurface = font.render(text, True, COLOR_WRITE)
        return textSurface

    # 开始游戏方法
    def startGame(self):
        _display.init()
        # 创建窗口加载窗口
        MainGame.window = _display.set_mode([MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT])
        # 创建我方坦克
        MainGame.TANK_P1 = Tank(400, 300)
        # 设置一下游戏标题
        _display.set_caption("坦克大战 "+version)
        # 让窗口持续刷新操作
        while True:
            # 给窗口完成一个填充颜色
            MainGame.window.fill(COLOR_BLACK)
            MainGame.window.blit(self.getTextSurface("剩余敌人:%d"%5),(5,5))
            MainGame.TANK_P1.displayTank()
            # 窗口的刷新
            _display.update()


MainGame().startGame()

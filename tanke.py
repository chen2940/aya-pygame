import pygame, sys

_display = pygame.display
_font = pygame.font
COLOR_BLACK = pygame.Color(0, 0, 0)
COLOR_RED = pygame.Color(255, 255, 255)
version = "1.03"
class MainGame():
    # 游戏主窗口
    window = None
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 800

    def __init__(self):
        pass

    def getTextSurface(self, text):
        _font.init()
        font = _font.SysFont("kaiti", 18)

        textSurface = font.render(text,True,)
        return textSurface

    # 开始游戏方法
    def startGame(self):
        _display.init()
        # 创建窗口加载窗口
        MainGame.window = _display.set_mode([MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT])
        # 设置一下游戏标题
        _display.set_caption("坦克大战 v%s"%version)
        # 让窗口持续刷新操作
        while True:
            # 给窗口完成一个填充颜色
            MainGame.window.fill(COLOR_BLACK)
            MainGame.window.blit((self.getTextSurface("剩余敌方数量%d辆"%5), 5.5))
            # 窗口的刷新
            _display.update()


MainGame().startGame()

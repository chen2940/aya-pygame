import pygame, sys

display = pygame.display
COLOR_BLACK = pygame.Color(0, 0, 0)


class MainGame():
    # 游戏主窗口
    window = None
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 800

    def init(self):
        pass

    # 开始游戏方法
    def startGame(self):
        display.init()
        # 创建窗口加载窗口
        MainGame.window = display.set_mode([MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT])
        # 设置一下游戏标题
        display.set_caption("坦克大战 v1.03")
        # 让窗口持续刷新操作
        while True:
            # 给窗口完成一个填充颜色
            MainGame.window.fill(COLOR_BLACK)
            # 窗口的刷新
            display.update()


MainGame().startGame()

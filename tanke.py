import pygame, sys

_display = pygame.display
_font = pygame.font
COLOR_BLACK = pygame.Color(0, 0, 0)
COLOR_WRITE = pygame.Color(255, 255, 255)
version = "0.01 Bate"


class MainGame():
    # 游戏主窗口
    window = None
    SCREEN_HEIGHT = 768
    SCREEN_WIDTH = 1024

    def __init__(self):
        pass

    def getEvent(self):
        # 1.获取所有事件
        eventList = pygame.event.get()
        # 2.对事件进行判断处理(1、点击关闭按钮 2、按下键盘上的某个按键)
        for event in eventList:
            # 判断 event.type 是否 QUIT，如果是退出的话，直接调用程序结束方法
            if event.type == pygame.QUIT:
                self.endGame()
            # 判断事件类型是否为按键按下，如果是，继续判断按键是哪一个按键，来进行对应的处理
            if event.type == pygame.KEYDOWN:
                # 具体是哪一个按键的处理
                if event.key == pygame.K_LEFT:
                    print("坦克向左调头，移动")
                    # 修改坦克方向
                    MainGame.TANK_P1.direction = 'L'
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_RIGHT:
                    print("坦克向右调头，移动")
                    # 修改坦克方向
                    MainGame.TANK_P1.direction = 'R'
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_UP:
                    print("坦克向上调头，移动")
                    # 修改坦克方向
                    MainGame.TANK_P1.direction = 'U'
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_DOWN:
                    print("坦克向下掉头，移动")
                    # 修改坦克方向
                    MainGame.TANK_P1.direction = 'D'
                    MainGame.TANK_P1.stop = False
                elif event.key == pygame.K_SPACE:
                    print("发射子弹")
                # 结束游戏方法
                if event.type == pygame.KEYUP:
                    # 松开的如果是方向键，才更改移动开关状态
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        # 修改坦克的移动状态
                        MainGame.TANK_P1.stop = True

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
        # 设置一下游戏标题
        _display.set_caption("坦克大战 "+version)
        # 让窗口持续刷新操作
        while True:
            # 给窗口完成一个填充颜色
            MainGame.window.fill(COLOR_BLACK)
            MainGame.window.blit(self.getTextSurface("剩余敌人:%d"%5),(5,5))
            # 窗口的刷新
            _display.update()


MainGame().startGame()

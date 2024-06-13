from random import random

import pygame, sys

_display = pygame.display
_font = pygame.font
COLOR_BLACK = pygame.Color(0, 0, 0)
COLOR_WRITE = pygame.Color(255, 255, 255)
version = "0.01 Bate"


class Tank():
    def __init__(self, left, top):
        self.speed = 1
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

    def endGame(self):
        print("谢谢使用")
        # 结束 python 解释器
        exit()

    # 坦克的移动方法
    def move(self):
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.height < MainGame.SCREEN_WIDTH:
                self.rect.left += self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < MainGame.SCREEN_HEIGHT:
                self.rect.top += self.speed

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


class EnemyTank(Tank):
    def init(self, left, top, speed):
        self.images = {
            'U': pygame.image.load('img/enemy1U.gif'),
            'D': pygame.image.load('img/enemy1D.gif'),
            'L': pygame.image.load('img/enemy1L.gif'),
            'R': pygame.image.load('img/enemy1R.gif')
        }
        self.direction = self.randDirection()
        self.image = self.images[self.direction]
        # 坦克所在的区域 Rect->
        self.rect = self.image.get_rect()
        # 指定坦克初始化位置 分别距 x，y 轴的位置
        self.rect.left = left
        self.rect.top = top
        # 新增速度属性
        self.speed = speed
        self.stop = True

    def randDirection(self):
        num = random.randint(1, 4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return 'L'
        elif num == 4:
            return 'R'


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
        MainGame.TANK_P1 = Tank(400, 300)
        # 设置一下游戏标
        _display.set_caption("坦克大战 " + version)
        # 让窗口持续刷新操作
        while True:
            # 给窗口完成一个填充颜色
            MainGame.window.fill(COLOR_BLACK)
            MainGame.window.blit(self.getTextSurface("剩余敌人:%d" % 5), (5, 5))
            MainGame.TANK_P1.displayTank()
            MainGame.TANK_P1.getEvent()
            MainGame.TANK_P1.move()
            # 窗口的刷新
            _display.update()


MainGame().startGame()

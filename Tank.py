import random
import pygame, config
from Baseitem import Baseitem
from Bullet import Bullet
from Music import Music


class Tank(Baseitem):
    def __init__(self, left, top):
        # 保存加载的图片
        self.images = {
            'U': pygame.image.load('img/p1tankU.gif'),
            'D': pygame.image.load('img/p1tankD.gif'),
            'L': pygame.image.load('img/p1tankL.gif'),
            'R': pygame.image.load('img/p1tankR.gif'),
        }
        self.direction = 'L'  # 方向
        self.image = self.images[self.direction]  # 根据图片方向获取图片
        self.rect = self.image.get_rect()  # 根据图片获取区域
        self.rect.left, self.rect.top = left, top
        self.speed = 5  # 移动速度
        self.stop = True  # 坦克移动开关
        self.live = True
        self.OldLeft = self.rect.left
        self.OldTop = self.rect.top

    # 移动
    def move(self):
        self.OldLeft = self.rect.left
        self.OldTop = self.rect.top
        # 判断坦克方向进行移动
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < config.SCREEN_HEIGHT:
                self.rect.top += self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.height < config.SCREEN_WIDTH:
                self.rect.left += self.speed

    # 射击
    def shot(self):
        return Bullet(self)

    def stay(self):
        self.rect.left = self.OldLeft
        self.rect.top = self.OldTop

    def hitWall(self):
        for wall in config.WallList:
            if pygame.sprite.collide_rect(self, wall):
                self.stay()

    # 展示坦克的方法
    def displayTank(self):
        # 获取展示对象
        self.image = self.images[self.direction]
        # 调用blit展示
        config.window.blit(self.image, self.rect)


class MyTank(Tank):
    def __init__(self, left, top):
        super(MyTank, self).__init__(left, top)

    def myTank_hit_enemyTank(self):
        for enemyTank in config.enemyTankList:
            if pygame.sprite.collide_rect(self, enemyTank):
                self.stay()


# 敌方坦克
class EnemyTank(Tank):
    def __init__(self, left, top, speed):
        super(EnemyTank, self).__init__(left, top)
        # 加载图片集
        self.images = {
            'U': pygame.image.load('img/enemy1U.gif'),
            'D': pygame.image.load('img/enemy1D.gif'),
            'L': pygame.image.load('img/enemy1L.gif'),
            'R': pygame.image.load('img/enemy1R.gif'),
        }
        # 随机生成方向
        self.direction = self.randDirection()
        self.image = self.images[self.direction]  # 根据方向获取图片
        self.rect = self.image.get_rect()  # 获取区域
        self.rect.left, self.rect.top = left, top  # 对left和top赋值
        self.speed = speed  # 速度
        self.flag = True  # 坦克移动开关
        self.step = 10  # 敌方坦克步数

    def enemyTank_hit_myTank(self):
        if pygame.sprite.collide_rect(self, config.my_tank):
            self.stay()

    def randDirection(self):
        nums = random.randint(1, 4)  # 生成1~4的随机整数
        if nums == 1:
            return "U"
        elif nums == 2:
            return "D"
        elif nums == 3:
            return "L"
        elif nums == 4:
            return "R"

    def randMove(self):  # 坦克的随机方向移动
        if self.step < 0:  # 步数小于0, 随机改变方向
            self.direction = self.randDirection()
            self.step = 50  # 步数复位
        else:
            self.move()
            self.step -= 1

    def shot(self):  # 重写shot方法
        num = random.randint(1, 1000)
        if num < 20 or num > 990:
            return Bullet(self)


###
def createMytank(left,top):  # 初始化我方坦克
    config.my_tank = MyTank(left, top)
    music = Music('img/start.wav')  # 创建音乐对象
    music.play()  # 播放音乐


def createEnemyTank(top, left):  # 初始化敌方坦克, 将敌方坦克添加到列表中
    for i in range(config.enemyTankCount):  # 生成指定敌方坦克数量
        aleft = random.randint(0, left)
        speed = random.randint(1, 4)
        enemy = EnemyTank(aleft, top, speed)
        config.enemyTankList.append(enemy)


def blitEnemyTank():
    for enemyTank in config.enemyTankList:
        if enemyTank.live:  # 判断敌方坦克状态
            enemyTank.displayTank()
            enemyTank.randMove()  # 调用子弹移动
            enemyTank.hitWall()
            if config.my_tank and config.my_tank.live:
                enemyTank.enemyTank_hit_myTank()
            if len(config.enemyBulletList) < 2:
                enemyBullet = enemyTank.shot()  # 敌方坦克射击
                if enemyBullet:  # 判断敌方坦克子弹是否为None
                    config.enemyBulletList.append(enemyBullet)  # 存储敌方坦克子弹
        else:
            config.enemyTankList.remove(enemyTank)

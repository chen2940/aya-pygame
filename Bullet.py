import pygame,config
from Baseitem import Baseitem
from Explode import Explode


#

class Bullet(Baseitem):
    def __init__(self, tank):
        self.image = pygame.image.load('img/enemymissile.gif')  # 图片加载
        self.direction = tank.direction  # 子弹的方向
        self.rect = self.image.get_rect()  # 获取区域
        if self.direction == 'U':  # 子弹的left和top与方向有关
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        self.speed = 10  # 子弹的速度
        self.live = True  # 子弹的状态

    # 移动
    def move(self):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                self.live = False  # 修改子弹的状态
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < config.SCREEN_WIDTH:
                self.rect.left += self.speed
            else:
                self.live = False  # 修改子弹的状态
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < config.SCREEN_HEIGHT:
                self.rect.top += self.speed
            else:
                self.live = False  # 修改子弹的状态
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.live = False  # 修改子弹的状态

    def hitWall(self):
        for wall in config.WallList:  # 循环遍历墙壁列表
            if pygame.sprite.collide_rect(self, wall):  # 检测子弹是否碰撞墙壁
                self.live = False  # 修改子弹状态
                wall.hp -= 1  # 碰撞后墙壁生命值减少
                if wall.hp <= 0:
                    wall.live = False

    # 子弹展示
    def displayBullet(self):
        # 将图片加载到窗口
        config.window.blit(self.image, self.rect)

    def myBullet_hit_enemyTank(self):
        for enemyTank in config.enemyTankList:
            if pygame.sprite.collide_rect(enemyTank, self):
                enemyTank.live = False
                self.live = False
                explode = Explode(enemyTank)
                config.explodeList.append(explode)

    def enemyBullet_hit_myTank(self):
        if config.my_tank and config.my_tank.live:
            if pygame.sprite.collide_rect(config.my_tank, self):
                explode = Explode(config.my_tank)  # 爆炸对象
                config.explodeList.append(explode)  # 将爆炸对象添加到爆炸列表中
                self.live = False  # 修改敌方子弹的状态
                config.my_tank.live = False  # 我方坦克的状态


#123
def blitMyBullet():  # 循环我方子弹列表, 并展示
    for myBullet in config.myBulletList:
        if myBullet.live:  # 判断子弹的状态
            myBullet.displayBullet()
            myBullet.move()
            myBullet.myBullet_hit_enemyTank()
            myBullet.hitWall()  # 检测我方坦克子弹是否碰撞
        else:
            config.myBulletList.remove(myBullet)


def blitEnemyBullet():  # 循环敌方子弹列表, 并展示
    for enemyBullet in config.enemyBulletList:
        if enemyBullet.live:
            enemyBullet.displayBullet()
            enemyBullet.move()
            enemyBullet.enemyBullet_hit_myTank()
            enemyBullet.hitWall()  # 检测敌方坦克子弹是否碰撞
        else:
            config.enemyBulletList.remove(enemyBullet)

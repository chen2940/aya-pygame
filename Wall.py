import pygame, config


#
def createWall(left,top,num):  # 初始化墙壁
    for i in range(num):
        wall = Wall(i * left, top)
        config.WallList.append(wall)


#123
def blitWall():
    for wall in config.WallList:
        if wall.live:
            wall.displayWall()
        else:
            config.WallList.remove(wall)


class Wall():
    def __init__(self, left, top):
        self.image = pygame.image.load('img/steels.gif')  # 加载墙壁图片
        self.rect = self.image.get_rect()  # 获取区域
        self.rect.left, self.rect.top = left, top  # 设置left, top
        self.live = True  # 存活状态
        self.hp = 3  # 设置墙壁生命值

    # 展示墙壁
    def displayWall(self):
        config.window.blit(self.image, self.rect)

import pygame
import tanke
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
        tanke.MainGame.window.blit(self.image, self.rect)

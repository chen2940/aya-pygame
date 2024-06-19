import pygame
import random
import time

_display = pygame.display
COLOR_BLACK = pygame.Color(0, 0, 0)
COLOR_RED = pygame.Color(255, 0, 0)
version = 'v1.25'


class MainGame:
    window = None
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 800
    TANK_P1 = None
    EnemyTank_list = []
    EnemyTank_count = 5
    Bullet_list = []
    Enemy_bullet_list = []
    Explode_list = []
    Wall_list = []

    @staticmethod
    def getTextSurface(text):
        pygame.font.init()
        font = pygame.font.SysFont('kaiti', 18)
        textSurface = font.render(text, True, COLOR_RED)
        return textSurface

    @staticmethod
    def createMyTank():
        MainGame.TANK_P1 = MyTank(370, 300)
        music = Music('img/start.wav')
        music.play()

    @staticmethod
    def createEnemyTank():
        top = 100
        for i in range(MainGame.EnemyTank_count):
            speed = random.randint(3, 6)
            left = random.randint(1, 7)
            eTank = EnemyTank(left * 100, top, speed)
            MainGame.EnemyTank_list.append(eTank)

    @staticmethod
    def createWalls():
        for i in range(6):
            wall = Wall(148 * i, 240)
            MainGame.Wall_list.append(wall)

    @staticmethod
    def blitWalls():
        for wall in MainGame.Wall_list:
            if wall.live:
                wall.displayWall()
            else:
                MainGame.Wall_list.remove(wall)

    @staticmethod
    def blitEnemyTank():
        for eTank in MainGame.EnemyTank_list:
            if eTank.live:
                eTank.displayTank()
                eTank.randMove()
                eTank.hitWalls()
                eTank.hitMyTank()
                eBullet = eTank.shot()
                if eBullet:
                    MainGame.Enemy_bullet_list.append(eBullet)
            else:
                MainGame.EnemyTank_list.remove(eTank)

    @staticmethod
    def blitBullet():
        for bullet in MainGame.Bullet_list:
            if bullet.live:
                bullet.displayBullet()
                bullet.bulletMove()
                bullet.hitEnemyTank()
                bullet.hitWalls()
            else:
                MainGame.Bullet_list.remove(bullet)

    @staticmethod
    def blitEnemyBullet():
        for eBullet in MainGame.Enemy_bullet_list:
            if eBullet.live:
                eBullet.displayBullet()
                eBullet.bulletMove()
                eBullet.hitWalls()
                if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                    eBullet.hitMyTank()
            else:
                MainGame.Enemy_bullet_list.remove(eBullet)




    @staticmethod
    def displayExplodes():
        for explode in MainGame.Explode_list:
            if explode.live:
                MainGame.Explode_list.remove(explode)
            else:
                explode.displayExplode()





    def getEvent(self):
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                self.endGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and not MainGame.TANK_P1:
                    self.createMyTank()
                if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                    if event.key == pygame.K_LEFT:
                        print("坦克向左调头,移动")
                        MainGame.TANK_P1.direction = 'L'
                        MainGame.TANK_P1.stop = False
                    elif event.key == pygame.K_RIGHT:
                        print("坦克向右调头，移动")
                        MainGame.TANK_P1.direction = 'R'
                        MainGame.TANK_P1.stop = False
                    elif event.key == pygame.K_UP:
                        print("坦克向上调头，移动")
                        MainGame.TANK_P1.direction = 'U'
                        MainGame.TANK_P1.stop = False
                    elif event.key == pygame.K_DOWN:
                        print("坦克向下调头,移动")
                        MainGame.TANK_P1.direction = 'D'
                        MainGame.TANK_P1.stop = False
                    elif event.key == pygame.K_SPACE:
                        print("发射子弹")
                        if len(MainGame.Bullet_list) < 3:
                            m = Bullet(MainGame.TANK_P1)
                            MainGame.Bullet_list.append(m)
                            music = Music('img/fire.wav')
                            music.play()
                        else:
                            print("子弹数量不足")
                        print("当前屏幕中的子弹数量为:%d" % len(MainGame.Bullet_list))
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                        MainGame.TANK_P1.stop = True

    def startGame(self):
        _display.init()
        MainGame.window = _display.set_mode([MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT])
        self.createMyTank()
        self.createEnemyTank()
        self.createWalls()
        _display.set_caption("坦克大战" + version)
        while True:
            MainGame.window.fill(COLOR_BLACK)

            self.getEvent()
            MainGame.window.blit(self.getTextSurface("剩余敌方坦克%d辆" % len(MainGame.EnemyTank_list)), (5, 5))
            if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                MainGame.TANK_P1.displayTank()
            else:
                del MainGame.TANK_P1
                MainGame.TANK_P1 = None
            if MainGame.TANK_P1 and not MainGame.TANK_P1.stop:
                MainGame.TANK_P1.move()
                MainGame.TANK_P1.hitWalls()
                MainGame.TANK_P1.hitEnemyTank()
            self.blitEnemyTank()
            self.blitBullet()
            self.blitEnemyBullet()
            self.displayExplodes()
            self.blitWalls()

            time.sleep(0.02)
            _display.update()


@staticmethod
def endGame():
    print("谢谢使用")
    exit()


class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Tank(BaseItem):
    def __init__(self, Left, top):
        super().__init__()
        self.images = {
            'U': pygame.image.load('img/p1tankU.gif'),
            'D': pygame.image.load('img/p1tankD.gif'),
            'L': pygame.image.load('img/p1tankL.gif'),
            'R': pygame.image.load('img/p1tankR.gif')
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = Left
        self.rect.top = top
        self.speed = 5
        self.stop = True
        self.live = True
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top

    def move(self):
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top
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


    def stay(self):
        self.rect.left = self.oldLeft
        self.rect.top = self.oldTop


    def hitWalls(self):
        for wall in MainGame.Wall_list:
            if pygame.sprite.collide_rect(wall, self):
                self.stay()


    def shot(self):
        return Bullet(self)


    def displayTank(self):
        self.image = self.images[self.direction]
        MainGame.window.blit(self.image, self.rect)


class MyTank(Tank):
    def __init__(self, Left, top):
        super(MyTank, self).__init__(Left, top)

    def hitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            if pygame.sprite.collide_rect(eTank, self):
                self.stay()


class EnemyTank(Tank):
    def __init__(self, Left, top, speed):
        super(EnemyTank, self).__init__(Left,top)
        self.images = {
            'U': pygame.image.load('img/enemy1U.gif'),
            'D': pygame.image.load('img/enemy1D.gif'),
            'L': pygame.image.load('img/enemy1L.gif'),
            'R': pygame.image.load('img/enemy1R.gif')
        }
        self.direction = self.randDirection()
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = Left
        self.rect.top = top
        self.speed = speed
        self.stop = True
        self.step = 30


    @staticmethod
    def randDirection():
        num = random.randint(1, 4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return 'L'
        elif num == 4:
            return 'R'


    def randMove(self):
        if self.step <= 0:
            self.direction = self.randDirection()
            self.step = 50
        else:
            self.move()
            self.step -= 1


    def shot(self):
        num = random.randint(1, 1000)
        if num <= 20:
            return Bullet(self)


    def hitMyTank(self):
        if MainGame.TANK_P1 and MainGame.TANK_P1.live:
            if pygame.sprite.collide_rect(self, MainGame.TANK_P1):
                self.stay()


class Bullet(BaseItem):
    def __init__(self, tank):
        super().__init__()
        self.image = pygame.image.load('img/enemymissile.gif')
        self.direction = tank.direction
        self.rect = self.image.get_rect()
        if self.direction == 'U':
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
        self.speed = 7
        self.live = True


    def bulletMove(self):
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                self.live = False
        elif self.direction == 'D':
            if self.rect.top < MainGame.SCREEN_HEIGHT - self.rect.height:
                self.rect.top += self.speed
            else:
                self.live = False
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.live = False
        elif self.direction == 'R':
            if self.rect.left < MainGame.SCREEN_WIDTH - self.rect.width:
                self.rect.left += self.speed
            else:
                self.live = False


    def displayBullet(self):
        MainGame.window.blit(self.image, self.rect)


    def hitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            if pygame.sprite.collide_rect(eTank, self):
                explode =Explode(eTank)
                MainGame.Explode_list.append(explode)
                music = Music('img/hit.wav')
                music.play()
                self.live = False
                eTank.live = False


    def hitMyTank(self):
        if pygame.sprite.collide_rect(self, MainGame.TANK_P1):
            explode = Explode(MainGame.TANK_P1)
            MainGame.Explode_list.append(explode)
            music = Music('img/hit.wav')
            music.play()
            self.live = False
            MainGame.TANK_P1.live = False


    def hitWalls(self):
        for wall in MainGame.Wall_list:
            if pygame.sprite.collide_rect(wall, self):
                self.live = False
                wall.hp -= 1
                if wall.hp <= 0:
                    wall.live = False


class Explode:
    def __init__(self, tank):
        self.rect = tank.rect
        self.step = 0
        self.images = [
            pygame.image.load('img/blast0.gif'),
            pygame.image.load('img/blast1.gif'),
            pygame.image.load('img/blast2.gif'),
            pygame.image.load('img/blast3.gif'),
            pygame.image.load('img/blast4.gif')
        ]
        self.image = self.images[self.step]
        self.live = True


    def displayExlode(self):
        if self.step < len(self.images):
            MainGame.window.blit(self.image, self.rect)
            self.image = self.images[self.step]
            self.step += 1
        else:
            self.live = False
            self.step = 0


class Wall:
    def __init__(self, Left, top):
        self.image = pygame.image.load('img/steels.gif')
        self.rect = self.image.get_rect()
        self.rect.left = Left
        self.rect.top = top
        self.live = True
        self.hp = 3


    def displayWall(self):
        MainGame.window.blit(self.image, self.rect)


class Music:
    def __init__(self, fileName):
        self.fileName = fileName
        pygame.mixer.init()
        pygame.mixer.music.load(self.fileName)


    @staticmethod
    def play():
        pygame.mixer.music.play()


if __name__ == "__main__":
    game = MainGame()
    game.startGame()

# 导入模块
import pygame, time, Bullet, Explode, Tank, Wall, config
from Music import Music


# 坦克类
class MainGame():

    def __init__(self):
        pass

    # 开始游戏
    def startGame(self):
        pygame.display.init()  # 加载主窗口
        config.window = pygame.display.set_mode([config.SCREEN_WIDTH, config.SCREEN_HEIGHT])  # 设置窗口大小并显示
        Tank.createMytank(350,300)
        Tank.createEnemyTank(100,600)  # 初始化敌方坦克
        Wall.createWall(145, 220, 6)  # 初始化墙壁
        # 窗口标题设置
        pygame.display.set_caption("坦克大战" + config.version)
        while True:
            time.sleep(0.02)
            # 颜色填充
            config.window.fill(config.BG_COLOR)
            # 获取事件
            self.getEvent()
            # 绘制文字
            config.window.blit(self.getTextSuface('敌方坦克剩余数量%d' % len(config.enemyTankList)), (10, 10))
            if config.my_tank and config.my_tank.live:
                config.my_tank.displayTank()  # 展示我方坦克
            else:
                del config.my_tank  # 删除我方坦克
                config.my_tank = None
            Tank.blitEnemyTank()  # 展示敌方坦克
            Bullet.blitMyBullet()  # 我方坦克子弹
            Bullet.blitEnemyBullet()  # 展示敌方子弹
            Explode.blitExplode()  # 爆炸效果展示
            Wall.blitWall()  # 展示墙壁
            if config.my_tank and config.my_tank.live:
                if not config.my_tank.stop:
                    config.my_tank.move()  # 调用坦克移动方法
                    config.my_tank.hitWall()
                    config.my_tank.myTank_hit_enemyTank()
            pygame.display.update()

    # 结束游戏
    def endGame(self):
        print('游戏结束')
        exit()  # 退出游戏

    # 文字显示
    def getTextSuface(self, text):
        pygame.font.init()  # 字体初始化
        font = pygame.font.SysFont('kaiti', 16)
        # 绘制文字信息
        textSurface = font.render(text, True, config.TEXT_COLOR)
        return textSurface

    # 事件获取
    def getEvent(self):
        # 获取所有事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 退出游戏
                self.endGame()
            # 键盘按键
            if event.type == pygame.KEYDOWN:
                if not config.my_tank:  # 当我方坦克不存在时, 按下Esc键重生
                    if event.key == pygame.K_p:
                        Tank.createMytank()
                if config.my_tank and config.my_tank.live:
                    # 上、下、左、右键的判断
                    if event.key == pygame.K_LEFT:
                        config.my_tank.direction = 'L'
                        config.my_tank.stop = False
                        print('左键, 坦克向左移动')
                    elif event.key == pygame.K_RIGHT:
                        config.my_tank.direction = 'R'
                        config.my_tank.stop = False
                        print('右键, 坦克向右移动')
                    elif event.key == pygame.K_UP:
                        config.my_tank.direction = 'U'
                        config.my_tank.stop = False
                        print('上键, 坦克向上移动')
                    elif event.key == pygame.K_DOWN:
                        config.my_tank.direction = 'D'
                        config.my_tank.stop = False
                        print('下键, 坦克向下移动')
                    elif event.key == pygame.K_ESCAPE:
                        self.endGame()
                    elif event.key == pygame.K_SPACE:
                        print('发射子弹')
                        if len(config.myBulletList) < 3:  # 可以同时发射子弹数量的上限
                            myBullet = Bullet.Bullet(config.my_tank)
                            config.myBulletList.append(myBullet)
                            music = Music('img/fire.wav')
                            music.play()
            # 松开键盘, 坦克停止移动
            if event.type == pygame.KEYUP:
                # 只有松开上、下、左、右键时坦克才停止, 松开空格键坦克不停止
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    if config.my_tank and config.my_tank.live:
                        config.my_tank.stop = True


if __name__ == '__main__':
    MainGame().startGame()

import pygame


class Music:
    def __init__(self, filename):
        self.filename = filename
        pygame.mixer.init()
        pygame.mixer.music.load(self.filename)  # 加载音乐

    # 音乐播放
    def play(self):
        pygame.mixer.music.play()
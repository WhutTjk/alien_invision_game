import pygame


class Ship:
    def __init__(self, screen):
        """初始化飞船，并且设置初始位置"""
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        # 获取图像对应的矩形框
        self.rect = self.image.get_rect()
        # 获取屏幕对应的矩形框
        self.screen_rect = screen.get_rect()
        # 将飞船图像位置进行定位，中心x为屏幕x，底部为屏幕底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

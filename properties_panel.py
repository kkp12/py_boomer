import pygame


class PropertiesPanel():

    def __init__(self):
        pass

    @staticmethod
    def build_text(content):
        my_font = pygame.font.SysFont("simsunnsimsun", 25)
        return my_font.render(content, True, (0, 0, 0))

    @staticmethod
    def draw_panel(screen, player_id, HP, speed, scope, bombs):
        text_surfaces = []
        text_surfaces.append(PropertiesPanel.build_text(str(HP)))
        text_surfaces.append(PropertiesPanel.build_text(str(speed)))
        text_surfaces.append(PropertiesPanel.build_text(str(scope)))
        text_surfaces.append(PropertiesPanel.build_text(str(bombs)))
        y = 70 if player_id == 1 else 350
        screen.blit(pygame.image.load(
            'resources/image/numback_2.png').convert_alpha(), (730, y))
        for i in range(len(text_surfaces)):
            screen.blit(text_surfaces[i], (735, y))
            y += 57
        pygame.display.flip()

    @staticmethod
    def draw_items(screen):
        # 画框
        screen.blit(pygame.image.load(
            'resources/image/state.png').convert_alpha(), (600, 0))

    @staticmethod
    def showHelp(screen):
        tips_board = pygame.image.load('resources/image/tips_boardhelp2.png')
        x, y = (80, 260)
        screen.blit(tips_board, (x, y))
        # 关闭帮助面板
        w, h = tips_board.get_size()
        first_y = 20
        screen.blit(PropertiesPanel.build_text(
            '操作说明'), (x + 230, y + first_y))
        screen.blit(PropertiesPanel.build_text(
            '玩家1：'), (x + 30, y + first_y + 30))
        screen.blit(PropertiesPanel.build_text(
            'W:上 A:左 S:下 D:右 空格:放炸弹'), (x + 30, y + first_y + 30 + 30))
        # screen.blit(PropertiesPanel.build_text(
        #     '空格:放炸弹'), (x + 30, y + first_y + 30 + 30 + 30))
        screen.blit(PropertiesPanel.build_text(
            '玩家2：'), (x + 30, y + first_y + 30 + 30 + 30))
        screen.blit(PropertiesPanel.build_text(
            '↑:上 ←:左 ↓:下 →:右 小键盘0：放炸弹'), (x + 30, y + first_y + 30 + 30 + 30 + 30))
        # screen.blit(PropertiesPanel.build_text(
        #     '0：放炸弹'), (x + 30, y + first_y + 30 + 30 + 30 + 30 + 30 + 30))
        screen.blit(PropertiesPanel.build_text(
            '制作人：'), (x + 30, y + first_y + 30 + 30 + 30 + 30 + 60))
        screen.blit(PropertiesPanel.build_text(
            '柯司博 匡乾 赖若潘 劳马东'), (x + 30, y + first_y + 30 + 30 + 30 + 30 + 60 + 30))
        return x, y, w

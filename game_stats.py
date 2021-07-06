class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # 游戏刚启动时处于活动状态
        self.game_active = False

        # 在任何情况下都不应重置最高得分
        self.high_score = self.get_stored_score()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def get_stored_score(self):
        """从本地获取最高分"""
        try:
            with open(self.ai_settings.high_score_file) as f_obj:
                high_score = f_obj.read()
                if high_score:
                    return int(high_score)
                else:
                    return 0
        except FileNotFoundError:
            return 0

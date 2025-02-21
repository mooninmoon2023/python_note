import sys
from datetime import datetime
from pathlib import Path

from loguru import logger
from threading import Lock


class Logger:
    _instance = None
    _lock = Lock()
    log_path = Path("./")

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialized = False
            return cls._instance


    def __init__(self):
        with self._lock:
            if not self._initialized:
                # 移除默认配置
                logger.remove()
                self._lg = logger
                # 初始化日志批次目录
                self.current_date = None
                self.current_round = None
                self.current_round_log_storage_path = None
                self.initialize()
                self._initialized = True


    def initialize(self):
        # 配置新的 logger
        log_format = "{time:YYYY-MM-DD HH:mm:ss} | {level} | {file} | {function} | {line} | {message}"

        ## 输出到终端
        self._lg.add(sys.stdout, level="DEBUG", format=log_format)

        ## 输出到文件
        ### 当天日志目录，如果此目录不存在则创建目录，使用 pathlib 实现而不是 os
        self.current_date = datetime.now().strftime("%Y-%m-%d")
        current_day_log_storage_path = self.log_path.joinpath(self.current_date)
        current_day_log_storage_path.mkdir(parents=True, exist_ok=True)

        ### 日志文件路径
        log_file_path = current_day_log_storage_path.joinpath(datetime.now().strftime("%Y-%m-%d %H-%M-%S.log"))
        self._lg.add(log_file_path, level="DEBUG", rotation="00:00", retention="7 days", compression="zip",
                     format=log_format)


    def get_logger(self):
        return self._lg


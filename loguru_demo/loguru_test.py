from loguru_config import Logger

logger = Logger().get_logger()

def loguru_test():
    logger.debug("debug 日志")
    logger.info("info 日志")
    logger.error("error 日志")
    logger.exception("exception 日志")
    logger.warning("warning 日志")

if __name__ == '__main__':
    logger.info("{name} 开始测试", name="")
    loguru_test()
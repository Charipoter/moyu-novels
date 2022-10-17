import json
import threading
from typing import IO, Any
from backend.utils.LoggingConfiger import logger
from backend.utils.IntervalTimeCaculator import IntervalTimeCaculator


class JsonProcess:

    @classmethod
    def load_json_as_io(cls, path: str) -> IO:
        return open(path, "r", encoding="utf-8")

    @classmethod
    def load_json_as_object(cls, path: str) -> Any:
        time = IntervalTimeCaculator()
        time.start()
        logger.info("开始读取json数据...")

        f = cls.load_json_as_io(path)
        try:
            o = json.load(f)
        except json.decoder.JSONDecodeError:
            f.close()
            cls.dump_to_json({}, path)
            return {}

        f.close()

        time.end()
        logger.info("json数据读取完毕，花费 %f 秒" % time.get_interval_time())

        return o

    @classmethod
    def dump_to_json_thread(cls, o: Any, path: str) -> None:
        time = IntervalTimeCaculator()
        time.start()
        logger.info("开始后台持久化数据...")

        f = open(path, "w", encoding="utf-8")
        json.dump(o, f)
        f.close()

        time.end()
        logger.info("后台持久化完毕，花费 %f 秒" % time.get_interval_time())

    @classmethod
    def dump_to_json(cls, o: Any, path: str) -> None:
        # 此方法应该多线程
        t = threading.Thread(target=cls.dump_to_json_thread, args=[o, path])
        t.start()
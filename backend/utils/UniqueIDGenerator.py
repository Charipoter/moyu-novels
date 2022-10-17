import datetime
import random


# 生成唯一id
class UniqueIDGenerator:

    # 超简易算法，时间戳+随机数，还是有可能重复的，如果你的手速达到了光速(?)
    @classmethod
    def easy_generate(cls) -> str:
        t = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        s = t + str(random.Random().randint(0, 9))
        return s

    @classmethod
    def generate_by_name_and_author(cls, name: str, author: str) -> int:
        # 我们希望，同一部小说id相同，且不同小说不同（类似hash）
        # 1.小说名 + 作者 = 唯一 , 如果找不到作者？ -> 给一个不可能的作者名
        # 2.小说名 + 网址 = 唯一 , 不同网站同一小说咋办？

        # 又或者无所谓是否相同，靠用户自己操作,只要唯一就行了

        # 尝试：直死无限 如倾如诉

        r = (name + author).__hash__()

        return r


if __name__ == "__main__":
    print(UniqueIDGenerator.generate_by_name_and_author("直死无限", "如倾如诉"))
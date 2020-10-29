from functools import partial

from decorator.deca import my_logger

class Demo:
    count: int = 2
    logger: my_logger = partial(my_logger, count)

    @logger()
    def main(self):
        return "in main function"


if __name__ == '__main__':
    d = Demo()
    d.main()

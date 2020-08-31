from colorama import Fore, Back, Style


class logConfig:
    LOG_LEVEL = "DEBUG"

    LOG_ENABLED = True
    LOG_TO_FILE = True
    LOG_PATH = '/home/benny/PycharmProjects/2_BennyJane/Learning_Py_World/log'
    # LOG_FORMAT = '%(asctime)s %(process)d %(levelname)s [%(pathname)s %(funcName)s] [%(lineno)d]:\n%(message)s'
    LOG_FORMAT = '%(asctime)s %(process)d ' + Fore.GREEN + '%(levelname)s' + Fore.RESET + ' [%(pathname)s ' + Fore.GREEN + '%(funcName)s' + Fore.RESET + '] ' + Fore.YELLOW + '%(lineno)d' + Fore.RESET + ': ' + Fore.CYAN + '%(message)s' + Fore.RESET
    LOG_TO_CONSOLE = True

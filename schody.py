from time import *
from config import *

def config_test():
    try:
        if stairs_num != -27 and sunrise != -27 and sunset != -27 and brightness_day != -27 and brightness_night != -27:
            return 'Config OK!'
    except NameError, e:
        print "Set your preferences in config file!   ",
        return e


print config_test()

def start_day():
    '''
    Function switches lights to day mode.
    :return: True if everything went correct, error message otherwise.
    '''
    print "Day starts"

def start_night():
    '''
    Function switches lights to night mode.
    :return: True if everything went correct, error message otherwise.
    '''
    print "Day ends"


while True:
    if int(strftime("%H%M")) == sunrise:
        start_day()
        sleep(60)
    if int(strftime("%H%M")) == sunset:
        start_night()
        sleep(60)
    sleep(10)


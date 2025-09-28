import time
class TimeManager:
    def __init__(self):
        self.start = None
        self.elapsed_s = None
        self.formated_str = None

    def current(self):
        """return current time"""
        return time.time() #current moment
    
    def format_time(self, time_obj):
        """return %M:%S formated string of time recieved as arg"""
        return time.strftime("%M:%S", time.gmtime(time_obj))

    def elapsed(self, start_t):
        """recieve an time object and calculate elapsed time based on time object and return integer elapsed time value -->int"""
        return int(time.time() - start_t)

    #FAILEDTODO: make elapsed_reverse functional to function right for count-down
    # def elapsed_reverse(self, target):
    #     return int(
    #         target - time.time()
    #     )
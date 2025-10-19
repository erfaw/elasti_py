import datetime
class DateManager:
    def __init__(self):
        """"""
        self.today = None
        self.yesterday = None
        self.before_yesterday = None

    def current_date(self):
        return datetime.date.today()
    
    def yesterday_date(self):
        return self.today - datetime.timedelta(days=1)
    
    def before_yesterday_date(self):
        return self.today - datetime.timedelta(days=2)
    



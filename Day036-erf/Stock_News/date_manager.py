import datetime
class DateManager:
    def __init__(self):
        """hold date details"""
        self.today = self.current_date()
        self.yesterday = None
        self.before_yesterday = None

    def current_date(self) -> datetime.date:
        """return dt.date.today()"""
        return datetime.date.today()
    
    def yesterday_date(self):
        """return yesterday based on 'self.today' date"""
        return self.today - datetime.timedelta(days=1)
    
    def before_yesterday_date(self):
        """return day before yesterday based on 'self.today' date"""        
        return self.today - datetime.timedelta(days=2)
    



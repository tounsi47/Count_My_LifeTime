import datetime

today = datetime.date.today()
class input_age_reformulation :
    def __init__(self, year, month, day) :
        self.day = day
        self.month = month
        self.year = year
        self.AVERAGE_DAYS_PER_YEAR = 365.2425
        
    
    def retrieve_input_age(self) :
        self.birthdate = datetime.date(self.year, self.month, self.day)
        self.input_age = (today.year - self.birthdate.year) + (today.month -  self.birthdate.month)/12 + (today.day - self.birthdate.day)/self.AVERAGE_DAYS_PER_YEAR
        self.natural_input_age = int(self.input_age)
        self.rest_of_days = round((self.input_age - self.natural_input_age) * self.AVERAGE_DAYS_PER_YEAR)
        retreived_input_age = [self.natural_input_age, self.rest_of_days]
        return retreived_input_age
        

    

    

   

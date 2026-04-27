import datetime

today = datetime.date.today()
class input_age_reformulation :
    def __init__(self, day, month, year) :
        self.day = day
        self.month = month
        self.year = year
        
    
    def retrieve_input_age(self) :
        self.birthdate = [self.day, self.month, self.year]
        self.input_age = (today.year - self.birthdate[2]) + (today.month -  self.birthdate[1])/12 + (today.day - self.birthdate[0])/365
        self.natural_input_age = int(self.input_age)
        self.rest_of_days = int((self.input_age - self.natural_input_age) * 365)
        retreived_input_age = [self.natural_input_age, self.rest_of_days]
        return retreived_input_age
        

    

    

   

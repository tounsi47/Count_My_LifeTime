
from date_time_retrieving import today


class TimeUnites:
    def __init__(self, input_age ): 
       self.input_age = input_age
       self.AVERAGE_DAYS_PER_YEAR = 365.2425
    def convert_to_seconds(self) :
        age_in_seconds = round((self.input_age[0] * (self.AVERAGE_DAYS_PER_YEAR * 24 * 60 * 60))  + (self.input_age[1] * 86400))
        return age_in_seconds
    def convert_to_minutes(self):
        age_in_minutes = round((self.input_age[0] * (self.AVERAGE_DAYS_PER_YEAR * 24 * 60))  + (self.input_age[1] * 1440))
        return age_in_minutes
    def convert_to_hours(self) :
        age_in_hours = round((self.input_age[0] * (self.AVERAGE_DAYS_PER_YEAR * 24))  + (self.input_age[1] * 24))
        return age_in_hours
    def convert_to_days(self, birth_year):
        today_year_by_4 = today.year/4
        today_year_by_100 = today.year/100
        today_year_by_400 = today.year/400
        initial_bisextil_days1 = (today_year_by_4 + today_year_by_400)  - today_year_by_100

        
        birth_year_by_4 = birth_year//4
        birth_year_by_100 = birth_year//100
        birth_year_by_400 = birth_year//400
        initial_bisextil_days2 = (birth_year_by_4 + birth_year_by_400) - birth_year_by_100

        bisextil_days_difference =  initial_bisextil_days1 - initial_bisextil_days2

        age_in_days = round((self.input_age[0] * 365) + bisextil_days_difference + self.input_age[1])
        
        #age_in_days = (self.input_age[0] * self.AVERAGE_DAYS_PER_YEAR)  + (self.input_age[1])
        return age_in_days
    def convert_to_weeks(self) :
        age_in_weeks = round((self.input_age[0] * 52.1)  + (self.input_age[1] / 7))
        return age_in_weeks
    def convert_to_months(self) :
        age_in_months = round((self.input_age[0] * 12)  + ((self.input_age[1] / (self.AVERAGE_DAYS_PER_YEAR/12))))
        return age_in_months
    
class TimeUnites:
    def __init__(self, input_age ): 
       self.input_age = input_age
    def convert_to_seconds(self) :
        age_in_seconds = (self.input_age[0] * 31536000)  + (self.input_age[1] * 86400)
        return age_in_seconds
    def convert_to_minutes(self):
        age_in_minutes = (self.input_age[0] * 525600)  + (self.input_age[1] * 1440)
        return age_in_minutes
    def convert_to_hours(self) :
        age_in_hours = (self.input_age[0] * 8760)  + (self.input_age[1] * 24)
        return age_in_hours
    def convert_to_days(self):
        age_in_days = (self.input_age[0] * 365)  + (self.input_age[1])
        return age_in_days
    def convert_to_weeks(self) :
        age_in_weeks = (self.input_age[0] * 52.1)  + (self.input_age[1] / 52.1)
        return age_in_weeks
    def convert_to_months(self) :
        age_in_months = (self.input_age[0] * 12)  + ((self.input_age[1] / 365) * 12)
        return age_in_months
    
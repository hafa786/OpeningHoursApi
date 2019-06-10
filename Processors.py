# Processor class - having all the processing operations for input data
import json

class Processor():
    def __init__(self):
        self.foo = []
        
    def run(self,data):
        # data1 = jsonify(data)
        formated_data = json.loads(data)
        # print(formated_data)
        for single_data in formated_data:
            print("------------------------")
            day_of_week = single_data
            daily_data = formated_data[day_of_week]
            if self.checkOpenOrClose(daily_data) :
                print(self.convertHours(daily_data))
            else:
                print("close")
            print(day_of_week)
            print(daily_data)
        return True
    
    def checkOpenOrClose(self,data):
        if data != []:
            return True
        else:
            return False
    
    def findOpenining(self,data):
        print(len(data))
        return True
    
    def findClosing(self, data):
        print(len(data))
        return True
    
    def filteringData(self, data):
        if len(data)%2 != 0 and len(data) != 1:
            del data[0]; 
        print(len(data))
        return True
    
    def convertHours(self,data):
        timings = [];
        openingHour = '';
        standard_closing = "1 AM"
        scheduled_time = ''
        openingHours = []
        closingHours = []
        #self.filteringData(data)
        # filltered = [i for n, i in enumerate(data) if i not in data[n + 1:]]
        # print(filltered)
        for single in data:
            ##print(single)
            if single["type"] =='open':
                openingHours.append(single['value'])
            elif single["type"] == 'close':
                closingHours.append(single['value'])
        print(openingHours)
        print(closingHours)
        if len(openingHours) == len(closingHours):
            print("equal")
            for i in range(len(closingHours)):
                scheduled_time += (str(int(openingHours[i]/3600) - 12) + ' PM' if int(openingHours[i]/3600) > 12 else str(int(openingHours[i]/3600)) + ' AM' );
                scheduled_time += " - " + (str(int(closingHours[i]/3600) - 12) + ' PM' if int(closingHours[i]/3600) > 12 else str(int(closingHours[i]/3600)) + ' AM' );
        elif closingHours == []:
            scheduled_time += (str(int(openingHours[0]/3600) - 12) + ' PM' if int(openingHours[0]/3600) > 12 else str(int(openingHours[0]/3600)) + ' AM' );
            scheduled_time += " - " + standard_closing
        elif len(closingHours) > len(openingHours):
            opening = 0
            for i in range(len(closingHours)):
                try:
                    if openingHours[i] is not None:
                        opening = openingHours[i];
                        scheduled_time += (str(int(openingHours[i]/3600) - 12) + ' PM' if (int(openingHours[i]/3600) > 12) else str(int(openingHours[i]/3600)) + " PM" if (int(openingHours[i]/3600) == 12)   else str(int(openingHours[i]/3600)) + ' AM' );
                except:
                    pass;
                if opening != 0 and opening < closingHours[i] :
                    scheduled_time += " - " + (str(int(closingHours[i]/3600) - 12) + ' PM' if int(closingHours[i]/3600) > 12  else str(int(closingHours[i]/3600)) + ' AM' );              
        else:
            print("not equal")
        print(scheduled_time);         
        # for single in data:
        #     readable_time = int(single['value'])/3600
        #     if readable_time > 12 :
        #         readable_time = str(readable_time - 12)  + " PM"
        #     elif len(data) == 1:
        #         readable_time = str(readable_time) + " AM " + standard_closing
        #     else:
        #         readable_time = str(readable_time) + " AM "
        #     timings.append(readable_time)
        #     # print(single['value'])
        # for timing in timings:
        #     openingHour += timing
        return True;
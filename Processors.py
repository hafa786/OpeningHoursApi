# Processor class - having all the processing operations for input data
import json

class Processor():
    def __init__(self):
        self.foo = []
    
    # run the main functionality of the api    
    def run(self,data):
        # initializing the number of days
        days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
        formated_data = []
        result_value = []
        # loading the json data
        json_data = json.loads(data)
        # formating the data
        for i in range(len(json_data)):
            formated_data.append(json_data[days[i]])
        # traversing the formated data by handling especial cases as well
        for j in range(len(formated_data)):
            # case one : opening hours is empty 
            if formated_data[j] == [] :
                result_value.append(" : ".join([days[j].title() , "Closed"]))
            # case two : A restaurant might not be closed during the same day it can be closed on next day timing
            elif self.checkClosingHours(formated_data[j]) is False:
                # getting closing from the next day
                formated_data[j].append(formated_data[j+1][0])
                # removing that closing from the next day
                del formated_data[j+1][0];
                result_value.append( " : ".join( [days[j].title(), self.convertHours(formated_data[j]) ] ) )
            # Case for opening in multiple times open and close.
            else:
                result_value.append( " : ".join( [days[j].title(), self.convertHours(formated_data[j]) ] ) )
        return result_value
    
    # function checking the closing hours in the day provided data
    def checkClosingHours(self, datas):
        check = False
        for singledata in datas:
            if singledata["type"] == "close":
                check = True
        return check
    
    # converting the given data in hours - human readable format
    def convertHours(self,data):
        # Initializing openingHours,closingHours and final_result lists
        final_result = []
        openingHours = []
        closingHours = []
        # making fill the openingHours and closingHours
        for single in data:
            if single["type"] =='open':
                openingHours.append(single['value'])
            elif single["type"] == 'close':
                closingHours.append(single['value'])
        # check for having balanced opening and closing hours
        if len(openingHours) == len(closingHours):
            # traversing the closing and opening hours list 
            for i in range(len(closingHours)):
                # string for storing every single value
                scheduled_time = ''
                opening = int(openingHours[i]/3600)
                closing = int(closingHours[i]/3600)
                scheduled_time += str(opening - 12) + ' PM' if opening > 12 else str(opening) + ' AM';
                scheduled_time += " - " + (str(closing - 12) + ' PM' if closing > 12 else str(closing) + ' AM' );
                final_result.append(scheduled_time)            
        else:
            pass
        # joining final_results in one value
        return ", ".join(final_result);
    
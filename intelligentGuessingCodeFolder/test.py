import csv, re
from turtle import position


# with open('problemset1_submission.csv', 'rb') as csvfile:



def validateEmail(strEmail):
    if re.match("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", strEmail):
        return True
    return False
listEmail = []
with open('problemset1_submission.csv') as csv_file:
    csv = csv.reader(csv_file)

    for row in csv_file:
        item =str(row)
        for delimeter in [',']:
            item = item.replace(str(delimeter),' ')
        
        wordList = item.split()
        for word in wordList:
            if(validateEmail(word)):
                listEmail.append(word)
    
    for i in listEmail:
        print(position('@', i))
    
        



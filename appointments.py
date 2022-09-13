import csv
from importlib.abc import ResourceLoader

def getInput(csvFile):
    print("hello")

res = []

with open('input.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    linecount = 0
    for row in csv_reader:
        res.append(row)
    
print (res)
print(len(res))

class Appointment:

    def __init__(self, employee_id, name, department_id, title_code, step, apptDate):
        self.employee_id = employee_id
        self.name = name
        self.department_id = department_id

        self.title_code = title_code
        self.step = step
        self.appt_begin_date, self.appt_end_date = self.getDate(apptDate)
    
    def getDate(self, apptDate):
        begin = True
        start = ''
        end = ''
        for char in apptDate:
            if char != '|':
                if begin == True:
                    start += char
                else:
                    end += char
            else:
                begin = False
        return (start,end)


output = []

for person in res:
    print(person)
    i = 0 
    while len(person) > 2:
        appt = Appointment(person['employee_id'],person['name'], person['department_id' + i], person['title_code'+ i], person['step'+ i], person['appointment_period'+ i] )
        #some code to remove from the object like person.remove(key)
        i += 1
        if appt['enddate'] > today:
            output.append(appt)
    

with open('output.csv', mode='w') as csv_file:
    fieldnames = ['employee_id', 'name', 'birth_month', 'department_id', 'title_code', 'step', 'appt_begin_date', 'appt_end_date']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    #for loop with the write header over my output so each one gets written one by one
    
    


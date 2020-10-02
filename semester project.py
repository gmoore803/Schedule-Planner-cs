print("-"*110)
print('                                  Jacksonville State University                  ')
print('                                   Fall Semester 2019                            ')
print('                                   Grayson Moore                                 ')
print('                                               CS230                             ')
print('-'*110)
print('                                 Course Enrollment Simulation                    ')
print('  '*700)
print('-'*110)
print('----------------------------------- Jacksonville State University --------------------------------------------')
class courses:
    
    def __init__(self,name,number):
        self.name = name
        self.number = number

    def cname(self):
        return '{} {}'.format(self.name,self.number)



    
crs_1 = courses('Math','100')
crs_2 = courses('EGH','101')
crs_3 = courses('Geo','104')

        
name,name2,stunumber = input('First name:'), input('last name:'), input('Student Number:')

print('Hi welcome to JSU schedule planner ' + name , name2 )
print('Majors offered')
x = "Computer Science","Business","Mathmatics","Nursing","Engineering","Education"
for e in x:
        print(e)
print("\n")
print('Please enter the following information below ')
print("\n")
maj = input('Select major from offered Section: ')

print("\n")
print("\n")
print("---------------------Course selection--------------------")
print('EGH 101') 
print('MS 101')
print('Math 131')
print('Math 142')
print('Math 105')
print('Geo 109')
print('Cell 107')
print('Lab 110')
print('FA 1190')
print('SPH 1170')
print('SCI 1201')
print('EG 201')
print('STATS 221')
print('BS 901')
print('FCS 301')
print('SCI 2101')


print("\n")
print("\n")





loops = int(input("How many classes will you be enrolling in this semester:"))
inputs = []
for x in range(loops):
    inputs.append(input("Please enter desired course: "))

print("\n")


print("Thank you for completing your 2020 spring schedule")
print("You can view a text copy, GM9508.txt is the name of the file.")

with open('GM9508.txt', 'w') as f:
    f.write("                              Jacksonville State University")
    f.write("\n")
    f.write("                              CS-230")
    f.write("\n")
    f.write("                              Grayson Moore")
    f.write("\n")
    f.write("-"*150)
    f.write("\n")
    f.write("\n")
    f.write("\n")
    f.write(name)
    f.write("\n")
    f.write(maj)
    f.write("\n")
    f.write(stunumber)
    f.write("\n")
    f.write("\n")
    for item in inputs:
    
        f.write("%s\n" % item)
    f.write("\n")
    f.write("\n"*5)
    f.write("\n")
    f.write("-"*150)
    f.write("\n")
    f.write("-"*150)
    f.write("\n")
    f.write("Thank you for using my schedule planner simulation.")
    f.close()
        



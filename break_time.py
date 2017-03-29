import webbrowser
import time

break_num = 0
num_breaks = 3

print('Program Started at :')
print time.ctime()

while break_num < num_breaks:
    time.sleep(10)
    print ('Take a Break At')
    print time.ctime()
    webbrowser.open("https://www.youtube.com/watch?v=m9AT7H4GGrA")
    break_num = break_num + 1

print('Complete')


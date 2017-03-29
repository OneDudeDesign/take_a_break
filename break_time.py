import webbrowser
import time

break_num = 0
num_breaks = 3

# indicate when the program started
print('Program Started at :' + time.ctime())

# loop for three breaks
while break_num < num_breaks:
    # sleep at 10 seconds for testing
    #TODO change to one hour for production
    time.sleep(10)
    # indicate the breaktime
    print ('Take a Break At :' + time.ctime())
    webbrowser.open("https://www.youtube.com/watch?v=m9AT7H4GGrA")
    break_num = break_num + 1

print('Complete')


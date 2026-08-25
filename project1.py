import numpy as np 

#  Student Performance Analysis :- 

marks = np.array([[85,80,90],[70,75,65],[92,88,95],[60,72,68],[78,82,80]]) 

# Display :- 
'''
print(marks)
'''

# total marks by each student 
'''
count = 1
for i in marks:
    sum = 0
    for j in i:
        sum = sum + j
    print(f"Total Marks of {count} student is {sum}")
    count = count+1

'''
# average marks of each student :-

avg = np.mean(marks,axis=1)
'''
print(avg)
'''
#  average marks in each subject:- 
'''
print(np.mean(marks,axis=0))
'''
#  highest score in each subject :-
'''
print(np.max(marks,axis=0))
'''
#  lowest score in each subject :-
'''
print(np.min(marks,axis=0))
'''
# average marks above 80 :- 
'''
print(np.where(avg>80))
'''
#  pass or fail status :- 
'''
print(np.where(avg > 75,"pass","fail")) 
'''
# highest performing student :- 
'''
print(np.argmax(avg))
'''
# Standard deviation of each subject :- 
print(np.std(marks,axis=0))
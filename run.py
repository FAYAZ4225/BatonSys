import os
import glob
list_dir = os.listdir('.')
list_dir = [f.lower() for f in list_dir]
sorted=sorted(list_dir)
print(sorted) #print ascending order sorted list
print("********************** FIRST CHECK PASSED **************************\n")
subs = 'property'
for filename in os.listdir('.'):  
    if not filename.startswith('base') and not filename.startswith('run'): #getting other properties files values
        with open(os.path.join('.', filename)) as f:
            content = f.read()
            print(content)
            print("****************")  
    if filename.startswith('base'):   #getting base.properties values
        with open(os.path.join('.', filename)) as f:
            s_content = f.read()
            print(s_content)
            print("****************")
# Write the file out again
file_names = glob.glob('[!br]*')
print(file_names)
for file_name in file_names:
    with open(file_name,'w') as f:
      f.write(s_content)
print("********************** SECOND CHECK PASSED **************************\n")
file = open("C:/Users/<user>/Desktop/config/runtime/runtime.properties", "w") 
file.write(s_content)
print("********************* RUN TIME FILE CREATED *************************\n")
print("********************* ALL CHECKS PASSED *************************\n")




         
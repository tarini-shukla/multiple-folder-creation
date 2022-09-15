## make multiple folders
import os
path= 'C:\\TDATA\\WaterTable'
for i in range (0,69):
    os.chdir(path)
    Newfolder='Huger_' +str(i)
    os.makedirs(Newfolder)
    path2=path+'\\'+Newfolder
    os.chdir(path2)
    file_name1=""
    for k in range (2019, 2022, 1):
         file_name1="Huger_"+str(i)+"_0_"+str(k)+".txt"
         file=open(file_name1, 'x')
        
    print("created", k+1, " files")

print(' folder completed')

## adding text files in the newly created folders
## copy content of one text files in selected folder and files
for i in range(0,69):
 with open('C:\\TDATA\\2021\\DNDC_2021_FTs.txt', 'r') as firstfile, open('C:\\TDATA\\WaterTable\\Huger_' +str(i)+'\\Huger_'+str(i)+'_0_2021.txt', 'w') as secondfile:
    for line in firstfile:
        secondfile.write(line)
print('completed')

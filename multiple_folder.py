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


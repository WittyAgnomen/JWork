#put files in respective folder
import glob
import os

#get main directory
home=os.getcwd()
os.chdir('medium')
print ('chabged dir')

files=glob.glob("*jpg")
for f in files:
    try:
        if f[-5]=='1':
            os.rename(f, "./one/"+f)
        elif f[-5]=='2':
            os.rename(f, "./two/"+f)
        elif f[-5]=='3':
            os.rename(f, "./three/"+f)
        elif f[-5]=='4':
            os.rename(f, "./four/"+f)
        elif f[-5]=='5':
            os.rename(f, "./five/"+f)
    except:
        print ('error with '+ f +' at ' + f[-5])

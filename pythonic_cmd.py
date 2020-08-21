import os
import time
print("Enter the command:")
print("Or type 'help' to know the command and descritions")

#information functions
def os_info():
    out=os.name
    return out

def absolute_path():
    out=os.path.abspath('.')
    return out

def cwd():
    out=os.getcwd()
    return out

def list_dir_files():
    out=os.listdir()
    j=1
    for i in out:
        print('         ',j,'-',i)
        j=j+1
    return f"Total {j-1} items"

def list_dir():
    out=os.scandir()
    j=1
    for i in out:
        print('         ',j,'-',i)
        j=j+1
    return f"Total {j-1} items"

def timey():
    out=time.ctime()
    return out

def helpy():
    print('time:       Display the system time.')
    print('mkdir:      Creates a Directory.')
    print('os_info:    Gives info of os.')
    print('cwd:        Gives path of current working Directory.')
    print('ls:         Display the list of Directorys and files in the current Directory')
    print('ls_dir:     Display the list of Directorys.')
    print('cd:         Displays the name of or changes the current directory.')
    print('run:        Command used to run a application on system.')
    print('open:       Command used to open a file using default application.')
    print('rmdir:      Remove a Directory.')
    print('rename:     Rename a Directory.')
    



#operation functions:
change_dir=lambda x:os.chdir(x)

make_dir=lambda x:os.mkdir(x)

run_appl=lambda x:os.system(x)

remove_dir=lambda x:os.rmdir(x)

rename=lambda x:os.rename(x)

o=lambda x:os.system(x)

infos={'os_info':os_info,'cwd':cwd,'ls':list_dir_files,'time':timey,'ls_dir':list_dir,'help':helpy}

operations={'mkdir':make_dir,'cd':change_dir,'run':run_appl,'rmdir':remove_dir,'rename':rename,'open':o}

           
while(True):
    current_dir=cwd()
    operations['cd'](current_dir)
    print(current_dir,end=' ')
    
    a=input('>>').strip()
    b=a.split()[0]
            
    info_list=[i for i in infos]
    operation_list=[i for i in operations]

    if a=='exit':
        exit()
            
    elif a in info_list:
        print(infos[a]())
    
    elif a.split()[0] in operation_list:
        operations[b](a[len(b)+1:])
        
        

    elif a=='exit':
        exit()

    print()
    


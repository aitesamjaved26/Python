import os, shutil
path = r'E:/Datasets/' # Path of directory with front slashes
file_names=os.listdir(path)
folder_names =['Ai Files','PDF Files', 'Excel Files', 'Zip Files'] # Names of folders you want to create based on files in directory

for folder in range (0,4):
  if not os.path.exists(path+folder_names[folder]): #checking if folder already exists. If not create one.
    os.makedirs(path + folder_names[folder])

for file in file_names:
  if '.pdf' in file and not os.path.exists(path+'PDF Files/'+file): #checking files and moving in relevant folders 
    shutil.move(path + file, path+'PDF Files/'+file)
  elif '.ai'in file and not os.path.exists(path + 'AI Files/'+file):
    shutil.move(path +file,path + 'AI Files/'+file )
  elif '.xlsx' in file and not os.path.exists(path +'Excel Files'+file):
    shutil.move(path+file,path + 'Excel Files/'+file)
  elif '.zip' in file and not os.path.exists(path +'Zip Files'+file):
    shutil.move(path+file,path + 'Zip Files/'+file)


#this is working on files path

import os

randomFiles = ['Files2.txt','Sommething.txt']

for filename in randomFiles:
    print(os.path.join('C:\\User\\Jeri James', filename))#dont forget to add the filename part

print(os.getcwd())

os.chdir('C:\\Users\\Jeri James\\randomCode')
print(os.getcwd())

#root path begin in the root path
#relative relative to the programa current working directory
# . this directory
# .. This is the parent folder





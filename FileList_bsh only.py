import os

srcfilelist = []                                               # Declare empty list for list of file names

def srcfilefunc():
    # For loop to build file list of file names
    for root, dirs, files in os.walk("C:\Automation\scanning_scripts - tiger1"):
        for file in files:
            if file.endswith(".bsh"):                       # Looks for files ending in extention .bsh only
                srcfilelist.append(os.path.join(root, file))   # Adds .bsh filenames to "filelist"

# # While loop to print "filelist"
# a=0                                                       # Declare counter variable for while loop
# while a<len(filelist):
#     print(filelist[a])
#     a+=1
import pandas as pd
import os
import xlsxwriter

srcfilelist = []                                    # Declare empty list for list of file names
mylines = []                                        # Declare an empty list for lines of text
bshfilelist = []                                    # Declare an empty list for .bsh file names
a=0

def srcfilefunc():
    # For loop to build file list of file names
    for root, dirs, files in os.walk(r"C:\UsedScripts"):
        for file in files:
            if file.endswith(".bsh"):                       # Looks for files ending in extention .bsh only
                srcfilelist.append(os.path.join(root, file))   # Adds .bsh filenames to "filelist"

def extractbshfunc(srcfilelist):
    with open (srcfilelist, 'rt') as myfile:    # Open .bsh file for reading text.
        for myline in myfile:                           # For each line in the file,
            mylines.append(myline.rstrip('\n'))         # strip newline and add to list.

    # Locate and print all occurences of substring 'source(script_dir + "'

    start = 'source(script_dir + "'                     # substring proceeding .bsh file name
    end = '");'                                         # substring at end of .bsh file name
    for line in mylines:                                # string to be searched
      index = 0                                         # current index: character being compared
      while index < len(line):                          # While index has not exceeded string length,
        index = line.find(start, index)                 # Set index to first occurrence of "start"
        if index == -1:                                 # If nothing was found,
          break                                         # exit the while loop.
        bshfile=line[line.find(start)+len(start):line.rfind(end)]   # Pull .bsh filename from between start and end substrings
        if bshfile not in bshfilelist:                  # Check for duplicate
            bshfilelist.append(bshfile)                 # If not in list, add .bsh file names to bshfilelist
        index += len(start)                             # increment the index by the length of "start".

def exporttoexcel(bshfilelist):
    df = pd.DataFrame(bshfilelist)                                      # Create dataframe to export to .xlsx
    writer = pd.ExcelWriter('BSHFileList.xlsx', engine='xlsxwriter')    # Write dataframe to .xlsx
    df.to_excel(writer, sheet_name='Sheet 1', index=False)              # Export .xlsx
    writer.save()                                                       # Save .xlsx

srcfilefunc()

# While loop to print "filelist"                                                      # Declare counter variable for while loop
while a<len(srcfilelist):
    extractbshfunc(srcfilelist[a])
    # print(srcfilelist[a])
    a+=1




exporttoexcel(bshfilelist)


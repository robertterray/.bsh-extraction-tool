import pandas as pd

mylines = []                                        # Declare an empty list for lines of text
bshfilelist = []                                    # Declare an empty list for .bsh file names

srcfile=r"Twelve Chip Setup Autosampler_2-25.bsh"

with open (srcfile, 'rt') as myfile:    # Open .bsh file for reading text.
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
    # if bshfile not in bshfilelist:                  # Check for duplicate
    #     bshfilelist.append(bshfile)                 # If not in list, add .bsh file names to bshfilelist
    bshfilelist.append(bshfile)
    index += len(start)                             # increment the index by the length of "start".

print(bshfilelist)

df = pd.DataFrame(bshfilelist)                                      # Create dataframe to export to .xlsx
writer = pd.ExcelWriter('BSHFileList.xlsx', engine='xlsxwriter')    # Write dataframe to .xlsx
df.to_excel(writer, sheet_name='Sheet 1', index=False)              # Export .xlsx
writer.close()                                                     # Save .xlsx


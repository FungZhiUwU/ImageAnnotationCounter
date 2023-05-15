import os
folderLocation= r'D:\Tapway\Count'
listOfFile=os.listdir(folderLocation)
linecount=0

for files in listOfFile:
    with open(os.path.join(folderLocation,files),'r') as file:
        for i in file:
            linecount+=1

# MeetTimes = 0
# MeetTimes = input("Enter total meet times")

# while MeetTimes > 0:
#     minutes = input("Enter total meeting minutes")
#     minutes + minutes
#     if MeetTimes = 0:
#         break

print('\nFolder Location:', folderLocation)
print('\nFiles total:', len(listOfFile))
print('\nBounding box total:' , linecount)
print('\nTotal with 74/1000:', 'RM',linecount*0.074)
print('\nMoney as dollar:', 'RM',linecount*0.017*4.432)
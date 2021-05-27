
###create list for all rooms. ###
room1 = [20, 21, 23, 25, 22]
room2 = [27, 23, 25, 20, 30, 24]
room3 = [22, 23, 24, 22] 

rooms = [room1, room2, room3]
print(rooms)

###Define globals variables needed. ###
allroomsum = float(0)
allroomavg = 0
roomHI = 0          #Anything higher than 0 will be replace.
roomLOW = room1[0]  #set to 1st variable in room1.

### ---------------------------------------------------------------###
### a) display avg temp for each room and high low temp at the same time. ###
def EachRoomAvg(room,roomHI,roomLOW):

    roomsum = float(0)
    count = 0
    roomavg = 0

    for i in (room):
        roomsum = roomsum + i
        count += 1
        #print(roomsum, count)
        roomavg = roomsum / count
        #print("The avg temperture for room is ",roomavg)
        
        ##gather the highest and lowest temp for all rooms.##
        if i > roomHI:      
            roomHI = i
            #print("Hi temp",roomHI)
            
        elif i < roomLOW:
            roomLOW = i
    
    return roomavg,roomHI,roomLOW,roomsum,count
    
room1avg,roomHI,roomLOW, allroomsum1, count1 = EachRoomAvg(room1,roomHI,roomLOW)
print("The avg temperture for room1 is ", room1avg)

room2avg,roomHI,roomLOW, allroomsum2, count2 = EachRoomAvg(room2,roomHI,roomLOW)
print("The avg temperture for room2 is ", room2avg)

room3avg,roomHI,roomLOW, allroomsum3, count3 = EachRoomAvg(room3,roomHI,roomLOW)
print("The avg temperture for room3 is ", room3avg)

### ---------------------------------------------------------------###
### b) display avg temp for all room and highest and lowest. ###

print("The highest temperture for all rooms is", roomHI, "and the lowest temperture is",roomLOW)

## Using rooms to get the avgerage temp on all rooms. ##

#print(allroomsum1,allroomsum2,allroomsum3,count1,count2,count3)
print("The avg temperture for all room is ", (allroomsum1+allroomsum2+allroomsum3)/(count1+count2+count3))



### END ###
### ---------------------------------------------------------------###




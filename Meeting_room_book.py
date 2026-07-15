#(room_name, start_time, end_time)
conform_room_book=int(input("ENTER NUMBER OF CONFORM BOOKING : "))
room_booked=[]
for i in range(conform_room_book):
    room_name=input("Enter room name :")
    start_time=input("Enter meeting start time : ")
    end_time=input("Enter meeting end time : ")
    room_booked.append([room_name,start_time,end_time])
room_booked=tuple(room_booked)
print("---Conform Room Booked List---")
for booked in room_booked:
    print(f"Room name : {room_name} \nStart time : {start_time} \nEnd time : {end_time}")

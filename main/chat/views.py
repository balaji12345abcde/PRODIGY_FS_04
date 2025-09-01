from django.shortcuts import render,redirect
from .models import Room,Messages
def HomePage(request):
    if request.method=='POST':
        User=request.POST.get('user')
        room=request.POST.get('room')
        try:
            excist=Room.objects.get(Room_name__icontains=room)
        except Room.DoesNotExist:
            i=Room.objects.create(Room_name=room)
        return redirect('room',room_name=excist.Room_name,user_name=User)
    return render(request,'home.html')
def RoomPage(request,room_name,user_name):
    excist=Room.objects.get(Room_name__icontains=room_name)
    message=Messages.objects.filter(room=excist)
    context={
        "message":message,
        "user":user_name,
        "roomname":excist.Room_name,
    }
    return render(request,'room.html',context)
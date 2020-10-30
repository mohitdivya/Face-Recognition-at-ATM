from django.shortcuts import render,redirect
from django.http import HttpResponse
from pal.models import users,amount 
from django.contrib import messages
# Create your views here.

import face_recognition
import cv2
def face(loc):
    cam= cv2.VideoCapture(0)
    s,img= cam.read()
    if s:
        bid_image = face_recognition.load_image_file(loc)
        bid_face_encoding = face_recognition.face_encodings(bid_image)[0]

        small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)


        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        check = face_recognition.compare_faces(bid_face_encoding, face_encodings)

        print(check)
        if check[0]:
            return True

        else:
            return False


    
    

def home(request):
    return render(request,'welcome.html')


def login(request):
    if request.method=='POST':
        usernam=request.POST['username']
        if users.objects.filter(username=usernam).exists():
            print(usernam+ 'logged in')
            
            global obj 
            obj= users.objects.get(username=usernam)
           
            if face(obj.img)==True:
                return render(request,"Select.html",{'obj':obj})
            else:
                messages.info(request,'face-recognition failure')
                return redirect('/login')
           
        else:
            messages.info(request,'username does not exists')
            return redirect('/login')
    else:
         return render(request,'login.html')


def showinfo(request):
     username=obj.username
     value=amount.objects.get(username=username)
     return render(request,'showinfo.html',{'obj':obj , 'value':value}) 


def withdraw(request):
    if request.method=='POST':
       sub=int(request.POST['withdraw'])
       username=obj.username
       ob=amount.objects.get(username=username)
       initial=int(ob.balance)
       if initial>sub:
            res=initial-sub
            ob.balance=res
            ob.save()
            return render(request,'Select.html',{'obj':obj})
       else:
             messages.info(request,'Insufficient Balance')
             return redirect('withdraw')
    else:  
        username=obj.username
        value=amount.objects.get(username=username)
        return render(request,'withdraw.html',{'value':value}) 


def deposit(request):
    if request.method=='POST':
       add=int(request.POST['deposit'])
       username=obj.username
       ob=amount.objects.get(username=username)
       initial=int(ob.balance)
       res=initial+add
       ob.balance=res
       ob.save()
       return render(request,'Select.html',{'obj':obj})
    else:    
       return render(request,'deposit.html')    
            
def Select(request):
    return render(request,'Select.html')
   
 
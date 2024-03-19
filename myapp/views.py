from django.shortcuts import render
from django.http import HttpResponse
from collections import defaultdict
from .models import *
from .forms import *
from io import TextIOWrapper
from django.contrib import messages
from django_pandas.io import read_frame
import warnings
warnings.filterwarnings(action='once')
import os
import numpy as np
import pandas as pd
import random
import cv2
import tensorflow as tf
from keras.models import load_model
from collections import deque
from moviepy.editor import VideoFileClip
from keras.preprocessing import image
from gtts import gTTS
# Create your views here.
global loaded_model,data_img

def adminlogin1(request):
    return render(request, "adminlogin.html")

def adminloginentered(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        passwd=request.POST['upasswd']
        if uname =='admin' and passwd =='admin':
            return render(request,"adminloginentered.html")
        else:
            return HttpResponse("invalied credentials")
    return render(request, "adminloginentered.html")

def userdetails(request):
    qs=userModel.objects.all()
    return render(request,"userdetails.html",{"qs":qs})

def activateuser(request):
    if request.method =='GET':
        uname=request.GET.get('pid')
        print(uname)
        status='Activated'
        print("pid=",uname,"status=",status)
        userModel.objects.filter(id=uname).update(status=status)
        qs=userModel.objects.all()
        return render(request,"userdetails.html",{"qs":qs})

# Create your views here.
def index(request):
    return render(request,'index.html')

def logout(request):
    return render(request, "index.html")

def userlogin(request):
    return render(request,'userlogin.html')

def userregister(request):
    if request.method=='POST':
        form1=userForm(request.POST)
        if form1.is_valid():
            form1.save()
            print("succesfully saved the data")
            return render(request, "userlogin.html")
        else:
            print("form not valied")
            return HttpResponse("form not valid")
    else:
        form=userForm()
        return render(request,"userregister.html",{"form":form})

def userlogincheck(request):
    if request.method == 'POST':
        sname = request.POST['email']
        print(sname)
        spasswd = request.POST['upasswd']
        print(spasswd)
        try:
            check = userModel.objects.get(email=sname,passwd=spasswd)
            print(check)
            status = check.status
            print('status',status)
            if status == "Activated":
                request.session['email'] = check.email
                return render(request, 'userpage.html')
            else:
                messages.success(request,'user is not activated')
                return render(request, 'userlogin.html')
        except Exception as e:
            print('Exception is ',str(e))
            pass
        messages.success(request,'Invalid name and password')
        return render(request,'userlogin.html')
    
def prepare(img_path):
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
    x = tf.keras.preprocessing.image.img_to_array(img)
    x = x/255
    return np.expand_dims(x, axis=0)
loaded_model = tf.keras.models.load_model('model/model.h5')
data_img = []
def getLiveDetect():
        print("Streaming Started")
        # Open you default camera
        cap = cv2.VideoCapture(0)
        while (True):
            ret, frame = cap.read()
            cv2.imshow('Press Q to Exit & S to Save', frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                # Quit if 'q' is pressed
                break
            elif key == ord('s'):
                # Save the frame if 's' is pressed
                path = 'predictionData/'
                path=path+'/'+'saved_frame.jpg'
                cv2.imwrite(path, frame)
                print("Frame saved")
        cap.release()
        cv2.destroyAllWindows()
def checkspam(request):
    if request.method == 'POST':
        sname = request.POST.get('enter')
        getLiveDetect()
        path = 'predictionData/'
        path=path+'/'+'saved_frame.jpg'
        print(path)
        result = loaded_model.predict([prepare(path)])
        print(result)
        preds=np.argmax(result,axis=1)
        print(preds)
        categories = ['AC', 'Bed', 'Bench', 'Book', 'Cupboard', 'Currency notes', 'Doors', 'Fan', 'Light', 'Pen', 'Table', 'Window', 'airplane', 'car', 'cat', 'dog', 'flower', 'fruit', 'motorbike', 'person']
        prediction=categories[int(preds)]
        print(prediction)
        audioText = prediction
        tts = gTTS(text=audioText, lang='en')
        tts.save("project/statics/audio/output.mp3")
        return render(request, 'spamreport.html', {"object": prediction})
    return render(request, 'spaminput.html')

def adddata(request):
    return render(request,'spaminput.html')

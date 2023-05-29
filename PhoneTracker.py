#Authored by Abdul Rahman

from tkinter import *
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode


def loc_result(number):
    phoneNumber = phonenumbers.parse(number)
    Key = "bfba27605dfc4f5c8ede9c7efeb421f#"    #last digit of api key has been changed by author.
    
    yourLocation = geocoder.description_for_number(phoneNumber,"en")
    #print("location : "+yourLocation)
    tex.insert(END,"Location : " +yourLocation)

    yourServiceProvider = carrier.name_for_number(phoneNumber,"en")
    #print("service provider : "+yourServiceProvider)
    tex.insert(END,"\nSim : " +yourServiceProvider)

    geocodr = OpenCageGeocode(Key)
    query = str(yourLocation)
    results = geocodr.geocode(query)
    
    # Assigning the latitude and longitude values to the lat and lng variables
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    #print("Latitude :"+str(lat))
    #print("Longitude : "+str(lng))
    tex.insert(END,"\nLatitude : " +str(lat))
    tex.insert(END,"\nLongitude : "+str(lng))

    tex.insert(END,"\n------\n")


def loc():
    number = f"{num.get()}"
    loc_result(number)


tracker = Tk()
tracker.title("PHONE TRACKER")
tracker.geometry("500x500")

Label(tracker,text=" 📱 PHONE NUMBER TRACKER 📱",font=("Arial",17,"bold")).place(x=2,y=2)
Label(tracker,text="Enter phone number with country code",fg="red",font=("Arial",13,"bold")).place(x=12,y=50)

num = StringVar()
tracknumber= Entry(tracker,textvariable = num,width=40).place(x=100,y=100)

submit = Button(tracker,text = " Find Location ",font=("Arial",15),fg="green",command=loc).place(x =140,y=140)

tex=Text(tracker,bg="pink")
tex.place(x=6,y=200)

tracker.mainloop()

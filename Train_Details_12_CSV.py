#Vaibhav 
#Train Details with CSV Data
#Project
import os
import csv

D={}
c=1
end=0
Tup=("yes","YES","Yes","y","Y")
def end():#print Thank You
    global en
    end=1
    print("\t","*"*11,sep="")
    print("\t","*"," "*9,"*",sep="")
    print("\t","*","THANK YOU","*",sep="")
    print("\t","*"," "*9,"*",sep="")
    print("\t","*"*11,sep="")
    
def Project():
#Heading
    print("_"*60,sep="")
    print("\tTRAIN\tDETAILS")
    print("_"*60,sep="")
    print()

#Inputs
    def Add(D):
        global c
        F=open("Data.csv",'a',newline='')
        W=csv.writer(F)
        
        Num=int(input("Enter Train Number:"))
        Name=input("Enter Train Name:")
        WDay=input("Enter Working Days of Train:").split()
        Start=input("Enter Start Station:")
        End=input("Enter End Station:")
        EPrice=float(input("Enter Extra Price:"))
        Coach=int(input("Enter Number of Coaches:"))
        
        L=[Num,Name.upper(),WDay,Start,End,EPrice,Coach]
        W.writerow(L)
        
        D[c]=L
        c=c+1
        print()
        R=input("Add more?:")
        print()
        if R in Tup:
            Add(D)
        else:
            F.close()
            Menu()

#Delete
    def Delete(D):
        F=open("Data.csv",'w',newline="")
        W=csv.writer(F)
        c=0

        if len(D)==0:
            print('No records!')
        else:
            R=int(input("Enter Train number to remove record:"))
        for key in D:
            dat=D[key]
            if dat[0]==R:
                c=1
                del D[key]
                print("Removed!!")
                break
            
        for key in D:
            dat=D[key]
            W.writerow(dat)

        F.close()

        if c==0 and len(D)>0:
            print('No such record is available!')
        
        
        print()
        Menu()

#MODIFY
    def Modify(D):
        c=0
        F=open("Data.csv",'w',newline="")
        W=csv.writer(F)

        if len(D)==0:
            print('No records!')
        else:
            N=int(input("Enter Train number to modify record:"))
        for key in D:
            dat=D[key]
            if dat[0]==N:
                c=c+1
                print("Fields to modify")
                print("1) Start Station")
                print("2) End Station")
                print("3) Extra price")
                Col=input("Enter your choice:")
                if Col=='1':
                    Start=input("Enter New Start Station:")
                    dat[3]=Start
                elif Col=='2':
                    End=input("Enter New End Station:")
                    dat[4]=End
                elif Col=='3':
                    EPrice=float(input("Enter Extra Price:"))
                    dat[5]=EPrice
                
            W.writerow(dat)
        if c==0 and len(D)>0:
            print("No such Record is available!!")
        F.close()
        print()
        Menu()

    #Outputs
    def T_Price(D):
        print("Coach Class:\tPrice")
        print("  First:\t3000")
        print("  Second:\t2500")
        print("  Third:\t2000")
        print("  Sleeper:\t1200")
        print("  General:\t500")
        print("GST is 12%")
        print()
        Num=int(input("Enter Train No.:"))
        Clas=input("Enter Coach Class:")
        Clas=Clas.upper()
        print()
        if len(D)>0:
            for key in D:
                dat=D[key]
                if dat[0]==Num:
                    if Clas=="FIRST":
                        TP=dat[5]+(30*12)+3000
                    elif Clas=="SECOND":
                        TP=dat[5]+(25*12)+2500
                    elif Clas=="THIRD":
                        TP=dat[5]+(20*12)+2000
                    elif Clas=="SLEEPER":
                        TP=dat[5]+(12*12)+1200
                    else:
                        TP=dat[5]+(5*12)+500
                    break
            print("Total Price :",TP)
            print()
            Menu()
        else:
            print("No Records Available!!")
            print()
            Menu()

    
    def Days(D):
        c=0
        Day=input("Enter day to check working trains:")
        print()
        print("Available trains-")
        for key in D:
            dat=D[key]
            for x in dat[2]:
                if Day==x:
                    c=c+1
                    print(c,") ",dat[1],sep="")
                    
        if c==0:
            print("No Trains!!")
        print()
        Menu()

    
    def Train_Detail(D):
        c=0
        if len(D)==0:
            print("No records!")
        else:
            T=int(input("Enter train no. to check details:"))
        print()
        for key in D:
            dat=D[key]
            if dat[0]==T:
                c=1
                print("Train Number-\t",dat[0])
                print("Train Name-\t",dat[1])
                print("Working Days-\t",end=" ")
                for x in dat[2]:
                    print(x,end=" ")
                print()
                print("Start Station-\t",dat[3])
                print("End Station-\t",dat[4])
                print("Extra Price-\t",dat[5])
                print("Number of Coaches-",dat[6])
                print()
                break
        if c==0 and len(D)>0:
            print("No such train is available")
        E3=input("Press Enter To Exit")
        print()
        R=input("View more?:")
        print()
        if R in Tup:
            Train_Detail(D)
        else:
            Menu()
            
    
    def Overall_Details(D):
        c=0
        for key in D:
            c=c+1
            dat=D[key]
            print("Train Number-\t",dat[0])
            print("Train Name-\t",dat[1])
            print("Working Days-\t",end=" ")
            for x in dat[2]:
                print(x,end=" ")
            print()
            print("Start Station-\t",dat[3])
            print("End Station-\t",dat[4])
            print("Extra Price-\t",dat[5])
            print("Number of Coaches-",dat[6])
            print("*"*50,end="")
            print()
        if c==0:
            print("No Records!!")
            print()
        E3=input("Press Enter To Exit")
        print()
        Menu()

    def Available(D):
        Train=[]
        c=0
        for key in D:
            dat=D[key]
            Train.append(dat[1])
        Train.sort()
        print("Available Trains-")
        for x in Train:
            c=c+1
            print(c,") ",x,sep="")
        if c==0:
            print("No Trains!!")
        print()
        Menu()
    
#Menu
        
    def Menu():
        print("HELP  MENU")
        print("1 : Add-Records")
        print("2 : Delete-Records")
        print("3 : Modify-Records")
        print("4 : Available Trains")
        print("5 : Train-Detail")
        print("6 : Overall-Details")
        print("7 : Train on Specific Days")
        print("8 : Total-Price")
        print("\nAny Other Key To Exit!!")
        print()
        Menu=input("Enter your Choice:")
        print()
        if Menu=='1':
            Add(D)
        elif Menu=='2':
            Delete(D)
        elif Menu=='3':
            Modify(D)
        elif Menu=='4':
            Available(D)
        elif Menu=='5':
            Train_Detail(D)
        elif Menu=='6':
            Overall_Details(D)
        elif Menu=='7':
            Days(D)
        elif Menu=='8':
            T_Price(D)
        else:
            App()
            

    
#Start
            
    global c,D
    c=1
    D={}
    print("Days - Mon  Tue  Wed  Thu  Fri  Sat  Sun")
    print("Coach Classes - First  Second  Third  Sleeper  General")
    print()
    n=int(input("Enter number of Records:"))
    print()
    
    F=open("Data.csv",'w',newline='')
    W=csv.writer(F)
    for x in range(0,n):
        Num=int(input("Enter Train Number:"))
        Name=input("Enter Train Name:")
        WDay=input("Enter Working Days of Train:").split()
        Start=input("Enter Start Station:")
        End=input("Enter End Station:")
        EPrice=float(input("Enter Extra Price:"))
        Coach=int(input("Enter Number of Coaches:"))
        
        L=[Num,Name.upper(),WDay,Start,End,EPrice,Coach]
        W.writerow(L)
            
        D[c]=L
        c=c+1
        print()

    F.close()
    
    print()
    Menu()


#App Screen
    
import pygame#Modules
import sys
from pygame.locals import *
from colors import *

def AboutUs():
    pygame.init()
    screen = pygame.display.set_mode((400,500))#Screen size
    pygame.display.set_caption('ABOUT US')#Title
    
    font = pygame.font.SysFont("Times new Roman", 20)#Fonts, 20-->fontsize

    Data1="This is version 1.2"
    Text1=font.render(Data1, True, red)
    Data2="Developer: VAIBHAV GUPTA"
    Text2=font.render(Data2, True, red)
    Data3="This is a software to help you manage"
    Text3=font.render(Data3, True, black)
    Data4="the records of Train Details"
    Text4=font.render(Data4, True, black)
    Data5="FEATURES:"
    Text5=font.render(Data5, True, orange)
    Data6="1) Add New Records"
    Text6=font.render(Data6, True, black)
    Data7="2) Modify Records"
    Text7=font.render(Data7, True, black)
    Data8="3) View Specific Records"
    Text8=font.render(Data8, True, black)
    Data9="4) Check Price"
    Text9=font.render(Data9, True, black)
    Data10="5) Delete Specific Records"
    Text10=font.render(Data10, True, black)
    Data11="THANK YOU FOR USING US"
    Text11=font.render(Data11, True, red)
    
    done = True
    while done:
        for event in pygame.event.get():#User gave any inputs
            
            screen.fill(white)#paint the screen white
            mouse=pygame.mouse.get_pos()#pos of cursor in form of Tuple
            
            if event.type == pygame.QUIT:#Close button clicked
                counter=0
                done = False

            try:
                screen.blit(Text1,(50,15))#update/render the object position
                screen.blit(Text2,(50,40))
                screen.blit(Text3,(50,95))#Text
                screen.blit(Text4,(50,120))
                screen.blit(Text5,(50,155))
                screen.blit(Text6,(50,180))
                screen.blit(Text7,(50,205))
                screen.blit(Text8,(50,230))
                screen.blit(Text9,(50,255))
                screen.blit(Text10,(50,280))
                screen.blit(Text11,(50,350))
                
            except:#error due to display quit
                pass

        try:  
            pygame.display.flip()#update screen
        except:
            pass
                
    pygame.display.quit()#disable pygame screen
    if counter==0:
        App()
                       
    
def App(): #Display Menu
    pygame.init()
    screen = pygame.display.set_mode((400,500))
    pygame.display.set_caption('LOGIN')
    
    font = pygame.font.SysFont("Times new Roman", 50)
    font2=pygame.font.SysFont("Times new Roman", 30)
    font3=pygame.font.SysFont("Times new Roman", 25)
    font4=pygame.font.SysFont("Times new Roman", 35)
    
    image=pygame.image.load("images.jpg")
    image=pygame.transform.scale(image,(75,75)) #Scaling
    
    done = True#condition for loop
    
    Title=font.render("RAILWAYS", True, blue) #Heading
    
    Id_Text="Login-Id" #id
    Id=font3.render(Id_Text, True, (255,255,255))#(255,255,255)-->white color
    rect = Id.get_rect()
    
    Submit=font2.render("SUBMIT", True, (255,255,255))
    
    pwd_Text="Password" #pwd
    password="Password"
    pwd=font3.render(pwd_Text, True, (255,255,255))
    rect2=pwd.get_rect()
    
    Exit=font.render("EXIT", True, (255,255,255))
    
    Type=False #For typing login ids after mouse is clicked
    Type2=False

    Move=pygame.image.load("preview.jpg")
    Move=pygame.transform.scale(Move,(300,80))
    
    MOVETRAIN=pygame.USEREVENT+1#user defined event
    pygame.time.set_timer(MOVETRAIN,300)#repeat after 0.3s
    ADDTRAIN=pygame.USEREVENT+2
    pygame.time.set_timer(ADDTRAIN,20000)
    x=350
    while done:
        for event in pygame.event.get():

            About=font4.render("About Us",True,Green) #About
            
            if event.type==MOVETRAIN:#Move Train with speed
                x-=10
            if event.type==ADDTRAIN:#Add Train at new Position
                x=350
            
            button1,button2,button3,button4=black,black,black,black
            
            screen.fill(white)
            mouse=pygame.mouse.get_pos()
            
            if event.type == pygame.QUIT:
                done = False
                
            if event.type==pygame.KEYDOWN and Type:#Button pressed
                if event.key==pygame.K_BACKSPACE:
                    if Id_Text=="Login-Id":
                        Id_Text=""
                    elif len(Id_Text)>0:
                        Id_Text=Id_Text[:-1]#erase last char
                else:
                    Id_Text += event.unicode#Add char
                Id=font3.render(Id_Text, True, (255,255,255))
                rect.size = Id.get_size()

            if event.type==pygame.KEYDOWN and Type2:
                if event.key==pygame.K_BACKSPACE:
                    if pwd_Text=="Password":
                        pwd_Text=""
                        password=""
                    elif len(pwd_Text)>0:
                        pwd_Text=pwd_Text[:-1]
                        password=password[:-1]
                else:
                    pwd_Text += "*"
                    password += event.unicode
                pwd=font3.render(pwd_Text, True, (255,255,255))
                rect2.size = Id.get_size()

            if event.type==pygame.MOUSEBUTTONDOWN:#Mouse clicked
                if 100<mouse[0]<320 and 150<mouse[1]<190:#id
                    Type=True
                else:
                    Type=False
                
                if 150<mouse[0]<270 and 300<mouse[1]<350:#submit
                    if Id_Text=="vaibhav" and password=="gupta":
                        done=False
                        pygame.display.quit()
                        
                        Project()#start main program
                
                if 100<mouse[0]<320 and 230<mouse[1]<270:#pwd
                    Type2=True
                else:
                    Type2=False

                if 135<mouse[0]<270 and 370<mouse[1]<405:#About
                    counter=1
                    done=False
                
                if 150<mouse[0]<270 and 430<mouse[1]<480:#exit
                    done = False
                    
            #Change Button color on hovering        
            if 100<mouse[0]<320 and 150<mouse[1]<190:#id
                button1=brown
            if 150<mouse[0]<270 and 300<mouse[1]<350:#submit
                button4=brown
            if 100<mouse[0]<320 and 230<mouse[1]<270:#pwd
                button3=brown
            if 135<mouse[0]<270 and 370<mouse[1]<405:#About
                About=font4.render("About Us",True,Blue)
            if 150<mouse[0]<270 and 430<mouse[1]<480:#exit
                button2=brown

            try:
                screen.blit(Move,(x,55))
                
                screen.blit(Title,(90,10))#Heading
                screen.blit(About,(135,370))#About
                
                pygame.draw.rect(screen,button1, pygame.Rect(100, 150, 220, 40))#Draw Rectangle
                screen.blit(Id,(100,150))#id
                
                pygame.draw.rect(screen,button3, pygame.Rect(100, 230, 220, 40))
                screen.blit(pwd,(100,230))#Password
                
                pygame.draw.rect(screen,button4, pygame.Rect(150, 300, 120, 50))
                screen.blit(Submit,(150,300))#Submit
                
                pygame.draw.rect(screen,button2, pygame.Rect(150, 430, 120, 50))
                screen.blit(Exit,(150,430))#exit
                
                screen.blit(image,(0,0))
            except:
                pass
        try:  
            pygame.display.flip()
        except:
            pass
        
    pygame.display.quit()
    try:
        if counter==1:
            AboutUs()
    except:
        pass

#RUN  
App()

end()
             

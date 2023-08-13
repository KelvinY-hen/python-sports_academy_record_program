#KELVIN YELIANDI
#TP058423
#test

def Coach_Append():
    print ("\n======================\nInputting New Coach Record\n=====================\n")
    check='1'
    while check=='1':
        BreakCode="n"
        Coachhandler=open("Coach.txt","r")
        CoachID=input("CoachID: ")
        for Coach in Coachhandler:
            Coach=Coach.strip()
            Coach=Coach.split(",")
            if CoachID==Coach[0]:
                BreakCode="y"
        Coachhandler.close()
        if BreakCode=="y":
            print ("CoachID is not Available")
            continue
        CoachName=input("Name: ")
        DateJoined=input("Date Joined: ")
        DateTerminated=input ("Date Terminated: ")
        HourlyRate=float(input ("Hourly Rate(RM): "))
        if HourlyRate>500.00 or HourlyRate<100.00:
            print("Invalid Rate")
            continue
        try:
            Phone= int(input("Phone Number: "))
        except:
            print ("Invalid Phone Number: ")
            continue
        Address= input("Address: ")
        check='2'
    while check=='2':
        SportCentreCode= input ("Sport Centre Code: ")
        SportCentreName= input ("Sport Centre Name: ")
        SportCentreName=SportCentreName.replace(" ","")
        Sporthandler=open("Sports.txt","r")
        for Sports in Sporthandler:
            Sports=Sports.strip()
            Sports=Sports.split(",")
            if SportCentreCode==Sports[2]:
                if SportCentreName.lower()!=Sports[3].lower():
                    BreakCode="y"
            elif SportCentreCode!=Sports[2]:
                if SportCentreName.lower()==Sports[3].lower():
                    BreakCode="y"
        Sporthandler.close()
        if BreakCode=="y":
            print("Sport Centre/Sport Centre Code does not match!\n")
            continue
        SportCode= input("Sport Code: ")
        SportName= input("Sport Name: ")
        SportName=SportName.replace(" ","")
        Sporthandler=open("Sports.txt","r")
        for Sports in Sporthandler:
            Sports=Sports.strip()
            Sports=Sports.split(",")
            if SportCode==Sports[0]:
                if SportName.lower()!=Sports[1].lower():
                    BreakCode="y"
            elif SportCode!=Sports[0]:
                if SportName.lower()==Sports[1].lower():
                    BreakCode="y"
        Sporthandler.close()
        if BreakCode=="y":
            print("SportID/Sport does not match!\n")
            continue
        check='3'
    while check=='3':
        Rating= int(input("Rating (1-5): "))
        if Rating<=0 or Rating>=6:
            print ("Invalid Rating")
            continue
        check="done"
    HourlyRate=str(HourlyRate)
    Phone= str(Phone)
    TotalRating=0
    TotalRating=TotalRating+Rating
    Rating= str (Rating)
    TotalRating=str(TotalRating)
    Feedback="1"
    Coachfile=open('Coach.txt','a')
    Coachfile.write(CoachID+","+CoachName+","+DateJoined+","+DateTerminated+","+HourlyRate+","+Phone+","+Address+","+SportCentreCode+","+SportCentreName+","+SportCode+","+SportName+","+Rating+","+Feedback+","+TotalRating+"\n")
    Coachfile.close()

def Coach_Display():
    print ("\n=====================\nDisplaying Coach Record\n=====================")
    choice="y"
    while choice=="y":
        Coachhandler=open('Coach.txt','r')
        Coachfile=Coachhandler.readlines()
        CoachNum=0
        num=1
        print("\n    Choose the Option")
        print("[ 1 ] All")
        for Coach in Coachfile:
            CoachNum+=1
            num+=1
            Coach=Coach.strip()
            Coach=Coach.split(",")
            print("[",num,"] CoachID:",Coach[0]," Name:",Coach[1])
    
        try:
            Selection=int(input("Enter the index number to view: "))
            if Selection>num or Selection<1:
                print("Number out of range")
                continue
            print(" ")
        except:
            print("Invalid Number")
            continue
        if Selection==1:
            CoachNum=0
            for Coach in Coachfile:
                Coach= Coach.strip()
                Coach= Coach.split(",")
                CoachNum+=1
                if CoachNum>1:
                    print ("====================")
                print("CoachID          : ",Coach[0])
                print("Name             : ",Coach[1])
                print("Date Joined      : ",Coach[2])
                print("Date Terminated  : ",Coach[3])
                print("Hourly Rate(RM)  : ",Coach[4])
                print("Phone Number     : ",Coach[5])
                print("Address          : ",Coach[6])
                print("Sport Centre Code: ",Coach[7])
                print("Sport Centre Name: ",Coach[8])
                print("Sport Code       : ",Coach[9])
                print("Sport Name       : ",Coach[10])
                print("Rating           : ",Coach[11])
                FeedNum=0
                Feedbackhandler= open ("Feedback.txt","r")
                for feedback in Feedbackhandler:
                    feedback=feedback.strip()
                    feedback=feedback.split(",")
                    if Coach[0]==feedback[0]:
                        FeedNum+=1
                        print("\t[",FeedNum,"]",feedback[1])
                Feedbackhandler.close()
                if feedback==0:
                    print("\tNo Feedback")
            Coachhandler.close()
        else:
            Coach=Coachfile[Selection-2]
            Coach= Coach.strip()
            Coach= Coach.split(",")
            print("CoachID          : ",Coach[0])
            print("Name             : ",Coach[1])
            print("Date Joined      : ",Coach[2])
            print("Date Terminated  : ",Coach[3])
            print("Hourly Rate(RM)  : ",Coach[4])
            print("Phone Number     : ",Coach[5])
            print("Address          : ",Coach[6])
            print("Sport Centre Code: ",Coach[7])
            print("Sport Centre Name: ",Coach[8])
            print("Sport Code       : ",Coach[9])
            print("Sport Name       : ",Coach[10])
            print("Rating           : ",Coach[11])
            FeedNum=0
            Feedbackhandler= open ("Feedback.txt","r")
            for feedback in Feedbackhandler:
                feedback=feedback.strip()
                feedback=feedback.split(",")
                if Coach[0]==feedback[0]:
                    FeedNum+=1
                    print("\t[",FeedNum,"]",feedback[1])
            Feedbackhandler.close()
            if feedback==0:
                print("\tNo Feedback")
        Repeat=input("\nBack to Display Menu?(y): ")
        if Repeat=="y":
            continue
        else:
            choice="n"
            break
        
def CoachID_Search ():
    Search="y"
    while Search=="y":
        print ("\n=====================\nCoachID Search\n=====================\n")
        Data=0
        try:
            IDsearch=input("Input CoachID: ")
        except:
            print ("Invalid ID")
            continue
        print ("====================")
        Coachfile=open('Coach.txt','r')
        for Coach in Coachfile:
            Coach= Coach.strip()
            Coach= Coach.split(",")
            if IDsearch == Coach[0]:
                Data+=1
                if Data>1:
                    print ("\n====================================")
                print("CoachID           : ",Coach[0])
                print("Name              : ",Coach[1])
                print("Date Joined       : ",Coach[2])
                print("Date Terminated   : ",Coach[3])
                print("Hourly Rate(RM)   : ",Coach[4])
                print("Phone Number      : ",Coach[5])
                print("Address           : ",Coach[6])
                print("Sport Centre Code : ",Coach[7])
                print("Sport Centre Name : ",Coach[8])
                print("Sport Code        : ",Coach[9])
                print("Sport Name        : ",Coach[10])
                print("Rating            : ",Coach[11])
                FeedNum=0
                Feedbackhandler= open ("Feedback.txt","r")
                for feedback in Feedbackhandler:
                    feedback=feedback.strip()
                    feedback=feedback.split(",")
                    if Coach[0]==feedback[0]:
                        FeedNum+=1
                        print("\t[",FeedNum,"]",feedback[1])
                Feedbackhandler.close()
                if feedback==0:
                    print("\tNo Feedback")
        Coachfile.close()
        if Data==0:
            print("No Specified Coach Found")
        else:
            print ("\n====================================")
        Search=input("\nDo you want to continue searching?(y): ")
    

def CoachRating_Search ():
    print ("\n=====================\nCoach Rating Search\n=====================\n")
    num=0
    Search="y"
    while Search=="y":
        try:
            Ratingsearch=int(input("Input Rating (1-5): "))
            if Ratingsearch>5 or Ratingsearch<1:
                print("out of range\n")
                continue
        except:
            print("Invalid Number\n")
            continue
        Ratingsearch=str(Ratingsearch)
        print (" ")
        Coachfile=open('Coach.txt','r')
        for Coach in Coachfile:
            Coach= Coach.strip()
            Coach= Coach.split(",")
            NoDecimal="{:.0f}".format(float(Coach[11]))
            NoDecimal=int(NoDecimal)
            NoDecimal=str(NoDecimal)
            if Ratingsearch == NoDecimal:
                num+=1
                if num>1:
                    print ("====================")
                print("CoachID          : ",Coach[0])
                print("Name             : ",Coach[1])
                print("Date Joined      : ",Coach[2])
                print("Date Terminated  : ",Coach[3])
                print("Hourly Rate(RM)  : ",Coach[4])
                print("Phone Number     : ",Coach[5])
                print("Address          : ",Coach[6])
                print("Sport Centre Code: ",Coach[7])
                print("Sport Centre Name: ",Coach[8])
                print("Sport Code       : ",Coach[9])
                print("Sport Name       : ",Coach[10])
                print("Rating           : ",Coach[11])
                FeedNum=0
                Feedbackhandler= open ("Feedback.txt","r")
                for feedback in Feedbackhandler:
                    feedback=feedback.strip()
                    feedback=feedback.split(",")
                    if Coach[0]==feedback[0]:
                        FeedNum+=1
                        print("\t[",FeedNum,"]",feedback[1])
                Feedbackhandler.close()
                if feedback==0:
                    print("\tNo Feedback")
        Coachfile.close()
        Search=input("\nDo you want to continue searching?(y): ")

def ModifyCoach ():
    print ("\n=====================\nModifying Coach Record\n=====================\n")
    Change1="y"
    while Change1=="y":
        Coachfile=open('Coach.txt','r')
        Coachfile=Coachfile.readlines()
        CoachCounter=0
        for Coach in Coachfile:
            Coach=Coach.strip()
            print ("[",CoachCounter+1,"]",Coach)
            CoachCounter+=1

        Coachnum= int(input("\nEnter number for coach you wanted to edit: "))
        print()
        if Coachnum>CoachCounter or Coachnum<=0:
            print("Out of Range")
            continue
        Change2="y"

        while Change2=="y":
            Selected_Coach=Coachfile[Coachnum-1].split(",")
            print("[1]  CoachID          : ",Selected_Coach[0])
            print("[2]  Name             : ",Selected_Coach[1])
            print("[3]  Date Joined      : ",Selected_Coach[2])
            print("[4]  Date Terminated  : ",Selected_Coach[3])
            print("[5]  Hourly Rate(RM)  : ",Selected_Coach[4])
            print("[6]  Phone Number     : ",Selected_Coach[5])
            print("[7]  Address          : ",Selected_Coach[6])
            print("[8]  Sport Centre Name: ",Selected_Coach[8])
            print("[9]  Sport Name       : ",Selected_Coach[10])
            print("[10] Rating           : ",Selected_Coach[11])
            Change3="y"

            while Change3=="y":
                try:
                    Selected_Attributes=int(input("\nEnter number for data part you wanted to edit: "))
                except:
                    print("Invalid Input")
                    continue
                if Selected_Attributes==8:
                    N=8
                elif Selected_Attributes==9:
                    N=10
                elif Selected_Attributes==10:
                    N=11
                else:
                    N=Selected_Attributes-1
                if Selected_Attributes==5 or Selected_Attributes==10:
                    try:
                        if Selected_Attributes==10:
                            print("Rating Range= 1-5")
                        New_AttVal=int(input ("Enter the new data: "))
                        if Selected_Attributes==10 and (New_AttVal>5 or New_AttVal<1):
                            print ("Invalid Rating")
                            continue
                    except:
                        print("Invalid Number")
                        continue
                elif Selected_Attributes==5:
                    try:
                        print("Valid Payrate range from 150.00 to 500.00")
                        New_AttVal=float(input ("Enter the new data: "))
                        if New_AttVal>500.00 or New_AttVal<100.00:
                            print("Invalid Payrate")
                            continue
                    except:
                        print("Invalid Payrate")
                elif Selected_Attributes>10 or Selected_Attributes<1:
                    print("Number out of range")
                    continue
                else:
                    New_AttVal=input ("Enter the new data: ")

                New_AttVal=str(New_AttVal)
                print ("Before: ",Selected_Coach[N].rstrip())
                print ("After : ",New_AttVal)
                if Selected_Attributes==12:
                    print("Proceeding with this changes will reset all feedback from the students")
                choice= input ("Do you want to proceed the changes?(y): ")
                if choice!="y":
                    continue
                if Selected_Attributes==8:
                    Sporthandle=open("Sports.txt","r")
                    checkcounter=0
                    New_AttVal=New_AttVal.replace(" ","")
                    for Sport in Sporthandle:
                        Sport=Sport.strip()
                        Sport=Sport.split(",")
                        SportName=str(Sport[1])
                        SportName=SportName.lower()
                        SportCentreName=str(Sport[3])
                        SportCentreName=SportCentreName.lower()
                        OldSport=Selected_Coach[10]
                        OldSport=OldSport.lower()
                        if (OldSport,New_AttVal.lower())==(SportName,SportCentreName):
                            Selected_Coach[7]=Sport[2]
                            New_AttVal=Sport[3]
                            checkcounter+=1
                    if checkcounter>1 or checkcounter<1:
                        print ("Invalid Sport Centre")
                        continue
                elif Selected_Attributes==9:
                    Sporthandle=open("Sports.txt","r")
                    checkcounter=0
                    New_AttVal=New_AttVal.replace(" ","")
                    for Sport in Sporthandle:
                        Sport=Sport.strip()
                        Sport=Sport.split(",")
                        SportName=str(Sport[1])
                        SportName=SportName.lower()
                        SportCentreName=str(Sport[3])
                        SportCentreName=SportCentreName.lower()
                        OldCentre=Selected_Coach[8]
                        OldCentre=OldCentre.lower()
                        if (New_AttVal.lower(),OldCentre)==(SportName,SportCentreName):
                            Selected_Coach[9]=Sport[0]
                            checkcounter+=1
                    if checkcounter>1 or checkcounter<1:
                        print ("Invalid Sport")
                        continue      
                if Selected_Attributes==10:
                    S='\n'
                    Selected_Coach[12]="1"
                    Selected_Coach[13]=New_AttVal+S
                    Feedbackhandler= open ("Feedback.txt","r")
                    Feedbackhandler=Feedbackhandler.readlines()
                    FeedbackNum=0
                    for feedback in Feedbackhandler:
                        feedback=feedback.strip()
                        feedback=feedback.split(",")
                        if Selected_Coach[0]==feedback[0]:
                            blank=""
                            Feedbackhandler[FeedbackNum]=blank
                        FeedbackNum+=1
                    
                    with open("Feedback.txt","w") as file:
                        file.writelines(Feedbackhandler)
                


                Selected_Coach[N]=New_AttVal
                Edited_Attributes=','.join(Selected_Coach)
                Coachfile[Coachnum-1]=Edited_Attributes

                with open("Coach.txt","w") as file:
                    file.writelines(Coachfile)
                Change3="n"
                
            print ("\nUpdate Succesful!")
            Change2=input ("Continue Changing Attributes? (y): ")
            if Change2=="y":
                print (" ")
                continue
        Change1=input ("Return to Select Coach Menu? (y): ")
        if Change1=="y":
            print (" ")
            continue

def CoachSort_Hourly():
    Coachhandler=open("Coach.txt","r")
    Coachfile=Coachhandler.readlines()  
    CoachNum=len(Coachfile)
    Num=0
    HourlyRate=[0 for i in range(CoachNum)]
    for Coach in Coachfile:
        Skip=0
        Coach=Coach.strip()
        Coach=Coach.split(",")
        ConvertedNum=float(Coach[4])
        for N in range(len(HourlyRate)):
            if HourlyRate[N]==ConvertedNum:
                Skip=1
                break
        if Skip==1:
            HourlyRate.pop(Num)
        else:
            HourlyRate[Num]=ConvertedNum
            Num+=1
    RateNum=len(HourlyRate)
    for i in range(RateNum):
        for j in range(0,RateNum-i-1):
            if HourlyRate[j]>HourlyRate[j+1]:
                HourlyRate[j],HourlyRate[j+1]=HourlyRate[j+1],HourlyRate[j]
    for N in range(RateNum):
        for Coach in Coachfile:
            Coach=Coach.strip()
            Coach=Coach.split(",")
            ConvertedNum=float(Coach[4])
            if HourlyRate[N]==ConvertedNum:
                print ("====================")
                print("CoachID          : ",Coach[0])
                print("Name             : ",Coach[1])
                print("Date Joined      : ",Coach[2])
                print("Date Terminated  : ",Coach[3])
                print("Hourly Rate(RM)  : ",Coach[4])
                print("Phone Number     : ",Coach[5])
                print("Address          : ",Coach[6])
                print("Sport Centre Code: ",Coach[7])
                print("Sport Centre Name: ",Coach[8])
                print("Sport Code       : ",Coach[9])
                print("Sport Name       : ",Coach[10])
                print("Rating           : ",Coach[11])
                FeedNum=0
                Feedbackhandler= open ("Feedback.txt","r")
                for feedback in Feedbackhandler:
                    feedback=feedback.strip()
                    feedback=feedback.split(",")
                    if Coach[0]==feedback[0]:
                        FeedNum+=1
                        print("\t[",FeedNum,"]",feedback[1])
                Feedbackhandler.close()
                if feedback==0:
                    print("\tNo Feedback")

def CoachSort_Name():
    Coachhandler=open("Coach.txt","r")
    Coachfile=Coachhandler.readlines()  
    CoachNum=len(Coachfile)
    Num=0
    NameStack=[0 for i in range(CoachNum)]
    for Coach in Coachfile:
        Skip=0
        Coach=Coach.strip()
        Coach=Coach.split(",")
        Name=Coach[1].replace(" ","")
        Name=Name.lower()
        for N in range(len(NameStack)):
            if NameStack[N]==Name:
                Skip=1
                break
        if Skip==1:
            NameStack.pop(Num)
        else:
            NameStack[Num]=Name
            Num+=1
    RateNum=len(NameStack)
    for i in range(RateNum):
        for j in range(0,RateNum-i-1):
            if NameStack[j]>NameStack[j+1]:
                NameStack[j],NameStack[j+1]=NameStack[j+1],NameStack[j]
    for N in range(RateNum):
        for Coach in Coachfile:
            Coach=Coach.strip()
            Coach=Coach.split(",")
            Name=Coach[1].replace(" ","")
            Name=Name.lower()
            if NameStack[N]==Name:
                print ("====================")
                print("CoachID          : ",Coach[0])
                print("Name             : ",Coach[1])
                print("Date Joined      : ",Coach[2])
                print("Date Terminated  : ",Coach[3])
                print("Hourly Rate(RM)  : ",Coach[4])
                print("Phone Number     : ",Coach[5])
                print("Address          : ",Coach[6])
                print("Sport Centre Code: ",Coach[7])
                print("Sport Centre Name: ",Coach[8])
                print("Sport Code       : ",Coach[9])
                print("Sport Name       : ",Coach[10])
                print("Rating           : ",Coach[11])

def CoachSort_Performance():
    Coachhandler=open("Coach.txt","r")
    Coachfile=Coachhandler.readlines()  
    CoachNum=len(Coachfile)
    Num=0
    Rating=[0 for i in range(CoachNum)]
    for Coach in Coachfile:
        Skip=0
        Coach=Coach.strip()
        Coach=Coach.split(",")
        ConvertedNum=float(Coach[11])
        for N in range(len(Rating)):
            if Rating[N]==ConvertedNum:
                Skip=1
                break
        if Skip==1:
            Rating.pop(Num)
        else:
            Rating[Num]=ConvertedNum
            Num+=1
    RateNum=len(Rating)
    for i in range(RateNum):
        for j in range(0,RateNum-i-1):
            if Rating[j]>Rating[j+1]:
                Rating[j],Rating[j+1]=Rating[j+1],Rating[j]
    for N in range(RateNum):
        for Coach in Coachfile:
            Coach=Coach.strip()
            Coach=Coach.split(",")
            ConvertedNum=float(Coach[11])
            if Rating[N]==ConvertedNum:
                print ("====================")
                print("CoachID          : ",Coach[0])
                print("Name             : ",Coach[1])
                print("Date Joined      : ",Coach[2])
                print("Date Terminated  : ",Coach[3])
                print("Hourly Rate(RM)  : ",Coach[4])
                print("Phone Number     : ",Coach[5])
                print("Address          : ",Coach[6])
                print("Sport Centre Code: ",Coach[7])
                print("Sport Centre Name: ",Coach[8])
                print("Sport Code       : ",Coach[9])
                print("Sport Name       : ",Coach[10])
                print("Rating           : ",Coach[11])

def Sport_Append():
    print ("\n======================\nInputting New Sport Record\n=====================")
    check="y"
    while check=="y":
        BreakCode="n"
        print(" ")
        SportID=input("SportID: ")
        SportName=input("Sport Name: ")
        SportName=SportName.replace(" ","")
        Sporthandler=open("Sports.txt","r")
        for Sports in Sporthandler:
            Sports=Sports.strip()
            Sports=Sports.split(",")
            if SportID==Sports[0]:
                if SportName.lower()!=Sports[1].lower():
                    BreakCode="y"
            elif SportID!=Sports[0]:
                if SportName.lower()==Sports[1].lower():
                    BreakCode="y"
            
        Sporthandler.close()
        if BreakCode=="y":
            print("SportID/Sport is already assigned!\n")
            continue
        SportCentreCode=input("Sport Centre Code: ")
        SportCentreName=input("Sport Centre: ")
        SportCentreName=SportCentreName.replace(" ","")
        Sporthandler=open("Sports.txt","r")
        for Sports in Sporthandler:
            Sports=Sports.strip()
            Sports=Sports.split(",")
            if SportCentreCode==Sports[2]:
                if SportCentreName.lower()!=Sports[3].lower():
                    BreakCode="y"
            elif SportCentreCode!=Sports[2]:
                if SportCentreName.lower()==Sports[3].lower():
                    BreakCode="y"
        Sporthandler.close()
        if BreakCode=="y":
            print("Sport Centre/Sport Centre Code is already assigned!\n")
            continue
        try:
            SportFee=int(input ("Sport Fee(RM): "))
            SportFee=str(SportFee)
        except:
            print ("Invalid Number")
            continue
        choice=input("\nDo you want to input this data as a new sport record?(y): ")
        if choice!="y":
            continue

        Sporthandler=open("Sports.txt","a")
        Sporthandler.write(SportID+","+SportName+","+SportCentreCode+","+SportCentreName+","+SportFee+"\n")
        Sporthandler.close()
        check=input("\nDo you want to continue input sport record?(y): ")
def SportSchedule_Append():
    print ("\n======================\nInputting Sport Schedule\n=====================\n")
    
    choice="y"
    while choice=="y":
        Sporthandler=open ("Sports.txt","r")
        Sportfile=Sporthandler.readlines()
        SportNum=0
        print("\n    Choose which sport to add schedule")
        for Sport in Sportfile:
            Sport=Sport.strip()
            Sport=Sport.split(",")
            print("[",SportNum+1,"] SportID:",Sport[0]," Sport:",Sport[1],"Sport Centre Code:",Sport[2],"Sport Centre Name:",Sport[3])
            SportNum+=1
        
        try:
            Selection=int(input("Enter the index number to add schedule: "))
            if Selection>SportNum or Selection<1:
                print("Number out of range")
                continue
            print(" ")
        except:
            print("Invalid Number")
            continue
        Sporthandler.close()
        
        Selected_Sport=Sportfile[Selection-1]
        Selected_Sport=Selected_Sport.strip()
        Selected_Sport=Selected_Sport.split(",")
        SportID=str(Selected_Sport[0])
        SportCentreCode=str(Selected_Sport[2])
        
        SportSchedule= open ("SportsSchedule.txt","a")
        
        Date=int(input("Enter Date: "))
        Date=str(Date)
        Month=input("Enter Month(Word): ")
        Time=input("Enter Time: ")
        Location=input("Enter Location: ")
        Coach=input("Enter Responsible Coach: ")
    
        SportSchedule.write(SportID+","+SportCentreCode+","+Date+","+Month+","+Time+","+Location+","+Coach+"\n")
        SportSchedule.close()
        
        choice=input("New Schedule Added!, Do you want to continue adding?(y): ")

def Sport_Display() :
    print ("\n=====================\nDisplaying Sport Record\n=====================")
    choice="y"
    while choice=="y":
        Sporthandler=open('Sports.txt','r')
        Sportfile=Sporthandler.readlines()
        SportNum=0
        num=1
        print("\n    Choose the Option")
        print("[ 1 ] All")
        for Sport in Sportfile:
            SportNum+=1
            num+=1
            Sport=Sport.strip()
            Sport=Sport.split(",")
            print("[",num,"] SportID:",Sport[0],",Sport:",Sport[1],",Sport Centre Code:",Sport[2],",Sport Centre Name:",Sport[3])
    
        try:
            Selection=int(input("Enter the index number to view: "))
            if Selection>num or Selection<1:
                print("Number out of range")
                continue
            print(" ")
        except:
            print("Invalid Number")
            continue
        if Selection==1:
            for Sport in Sportfile:
                SportSchedulehandler=open ("SportsSchedule.txt","r")
                SC=0
                Schedule=""
                Sport= Sport.strip()
                Sport= Sport.split(",")
                print ("\n====================================")
                print("SportID          : ",Sport[0])
                print("Sport Name       : ",Sport[1])
                print("Sport Centre Code: ",Sport[2])
                print("Sport Centre Name: ",Sport[3])
                print("Sport Fee        : ",Sport[4])
                print("Schedule         :")
                for Schedule in SportSchedulehandler:
                    Schedule=Schedule.strip()
                    Schedule=Schedule.split(",")
                    if (Sport[0],Sport[2])==(Schedule[0],Schedule[1]):
                        SC+=1
                        print ("\t\t   ====================")
                        print ("\t\t   Date: ",Schedule[2])
                        print ("\t\t   Month(Word): ",Schedule[3])
                        print ("\t\t   Time: ",Schedule[4])
                        print ("\t\t   Location: ",Schedule[5])
                        print ("\t\t   Responsible Coach: ",Schedule[6])
                SportSchedulehandler.close()
                if SC>1:
                    print ("\t\t   ====================")
                if SC==0:
                    print ("\tEMPTY")
        else:
            SportSchedulehandler=open ("SportsSchedule.txt","r")
            Sport=Sportfile[Selection-2]
            Sport= Sport.strip()
            Sport= Sport.split(",")
            SC=0
            print("SportID          : ",Sport[0])
            print("Sport Name       : ",Sport[1])
            print("Sport Centre Code: ",Sport[2])
            print("Sport Centre Name: ",Sport[3])
            print("Sport Fee        : ",Sport[4])
            print("Schedule         :")
            for Schedule in SportSchedulehandler:
                Schedule=Schedule.strip()
                Schedule=Schedule.split(",")
                if (Sport[0],Sport[2])==(Schedule[0],Schedule[1]):
                    SC+=1
                    print ("\t\t====================")
                    print ("\t\tDate: ",Schedule[2])
                    print ("\t\tMonth(Word): ",Schedule[3])
                    print ("\t\tTime: ",Schedule[4])
                    print ("\t\tLocation: ",Schedule[5])
                    print ("\t\tResponsible Coach: ",Schedule[6])
                if SC>1:
                     print ("\t\t====================")
            SportSchedulehandler.close()
        Repeat=input("\nBack to Display Menu?(y): ")
        Sporthandler.close()
        if Repeat=="y":
            continue
        else:
            choice="n"
            break

def SportID_Search ():
    Search="y"
    while Search=='y':
        print ("\n=====================\nSportID Search\n=====================\n")
        Data=0
        IDsearch=input("Input SportID: ")
        print ("====================")
        Sportsfile=open('Sports.txt','r')
        SportSchedulehandler=open ("SportsSchedule.txt","r")
        for Sport in Sportsfile:
            Sport= Sport.strip()
            Sport= Sport.split(",")
            if IDsearch in Sport[0]:
                Data+=1
                if Data>1:
                    print ("\n====================================")
                print("Sport Code        : ",Sport[0])
                print("Sport Name        : ",Sport[1])
                print("Sport Centre Code : ",Sport[2])
                print("Sport Centre Name : ",Sport[3])
                print("Sport Fee         : ",Sport[4])
                SC=0
                for Schedule in SportSchedulehandler:
                    Schedule=Schedule.strip()
                    Schedule=Schedule.split(",")
                    if (Sport[0],Sport[2])==(Schedule[0],Schedule[1]):
                        SC+=1
                        print ("\t\t====================")
                        print ("\t\tDate: ",Schedule[2])
                        print ("\t\tMonth(Word): ",Schedule[3])
                        print ("\t\tTime: ",Schedule[4])
                        print ("\t\tLocation: ",Schedule[5])
                        print ("\t\tResponsible Coach: ",Schedule[6])
                if SC>1:
                    print ("\t\t====================")
        if Data==0:
            print("No Sport with Inputted SportID Found")
        Sportsfile.close()
        SportSchedulehandler.close()
        
        Search=input("Do you want to continue searching?(y): ")


def ModifySport ():
    print ("\n=====================\nModifying Sport Record\n=====================\n")
    Change1="y"
    while Change1=="y":
        Sportfile=open('Sports.txt','r')
        Sportfile=Sportfile.readlines()
        SportCounter=0
        for Sport in Sportfile:
            Sport=Sport.strip()
            Sport=Sport.split(",")
            print("[",SportCounter+1,"] SportID:",Sport[0],",Sport:",Sport[1],",Sport Centre Code:",Sport[2],",Sport Centre Name:",Sport[3],",Sport Fee:",Sport[4])
            SportCounter+=1

        Sportnum= int(input("\nEnter Sport Index you wanted to edit: "))
        print()
        if Sportnum>SportCounter or Sportnum<=0:
            print("Out of Range")
            continue
        Change2="y"

        while Change2=="y":
            Selected_Sport=Sportfile[Sportnum-1].split(",")
            Attrnum=0
            for Attributes in Selected_Sport:
                print ("[",Attrnum+1,"]",Attributes)
                Attrnum+=1
            Change3="y"

            while Change3=="y":
                try:
                    Selected_Attributes=int(input("\nEnter number for data part you wanted to edit: "))
                    if Selected_Attributes>Attrnum or Selected_Attributes<1:
                        print ("Number out of range")
                except:
                    print ("Invalid Number")
                    continue
                if Selected_Attributes==4:
                    try:
                        New_AttVal=input ("Enter the new data: ")
                    except:
                        print ("Invalid Number")
                        continue
                else:
                    New_AttVal=input ("Enter the new data: ")

                New_AttVal=str(New_AttVal)
                print ("Before: ",Selected_Sport[Selected_Attributes-1].rstrip())
                print ("After : ",New_AttVal)
                choice= input ("Do you want to proceed the changes?(y): ")
                if choice!="y":
                    continue
                S="\n"
                Selected_Sport[Selected_Attributes-1]=New_AttVal
                Edited_Attributes=','.join(Selected_Sport)
                Sportfile[Sportnum-1]=Edited_Attributes+S

                with open("Sports.txt","w") as file:
                    file.writelines(Sportfile)
                Change3="n"
                
            print ("\nUpdate Succesful!")
            Change2=input ("Continue Changing Attributes? (y): ")
            if Change2=="y":
                print (" ")
                continue
        Change1=input ("Return to Select Sport Menu? (y): ")
        if Change1=="y":
            print (" ")
            continue       

def ModifySportSchedule ():
    print ("\n================================\nModifying Sport Schedule Record\n================================\n")
    Change1="y"
    while Change1=="y":
        SportSchedulefile=open('SportsSchedule.txt','r')
        SportSchedulefile=SportSchedulefile.readlines()
        SportScheduleCounter=0
        for SportSchedule in SportSchedulefile:
            SportSchedule=SportSchedule.strip()
            SportSchedule=SportSchedule.split(",")
            print ("================================")
            print ("[",SportScheduleCounter+1,"]\tSportID: ",SportSchedule[0])
            print ("\tSport Centre ID: ",SportSchedule[1])
            print ("\tDate: ",SportSchedule[2])
            print ("\tMonth(Word): ",SportSchedule[3])
            print ("\tTime: ",SportSchedule[4])
            print ("\tLocation: ",SportSchedule[5])
            print ("\tResponsible Coach: ",SportSchedule[6])
            SportScheduleCounter+=1
        if SportScheduleCounter>1:
            print ("================================")
        SportSchedulenum= int(input("\nEnter Sport Index you wanted to edit: "))
        print()
        if SportSchedulenum>SportScheduleCounter or SportSchedulenum<=0:
            print("Out of Range")
            continue
        Change2="y"

        while Change2=="y":
            Selected_SportSchedule=SportSchedulefile[SportSchedulenum-1].split(",")
            print ("[1]SportID: ",Selected_SportSchedule[0])
            print ("[2]Sport Centre ID: ",Selected_SportSchedule[1])
            print ("[3]Date: ",Selected_SportSchedule[2])
            print ("[4]Month(Word): ",Selected_SportSchedule[3])
            print ("[5]Time: ",Selected_SportSchedule[4])
            print ("[6]Location: ",Selected_SportSchedule[5])
            print ("[7]Responsible Coach: ",Selected_SportSchedule[6])
            Change3="y"

            while Change3=="y":
                Selected_Attributes=int(input("\nEnter number for data part you wanted to edit: "))
                New_AttVal=input ("Enter the new data: ")

                New_AttVal=str(New_AttVal)
                print ("Before: ",Selected_SportSchedule[Selected_Attributes-1].rstrip())
                print ("After : ",New_AttVal)
                choice= input ("Do you want to proceed the changes?(y): ")
                if choice!="y":
                    continue
                S=""
                if Selected_Attributes==7:
                    S="\n"
                Selected_SportSchedule[Selected_Attributes-1]=New_AttVal+S
                Edited_Attributes=','.join(Selected_SportSchedule)
                SportSchedulefile[SportSchedulenum-1]=Edited_Attributes

                with open("SportsSchedule.txt","w") as file:
                    file.writelines(SportSchedulefile)
                Change3="n"
                
            print ("\nUpdate Succesful!")
            Change2=input ("Continue Changing Attributes? (y): ")
            if Change2=="y":
                print (" ")
                continue
        Change1=input ("Return to Select Sport Menu? (y): ")
        if Change1=="y":
            print (" ")
            continue       


def RegStudent_Display():
   print ("\n====================================\nDisplaying Registered Students Record\n====================================")
   RegStudentFile=open("Student.txt","r")
   for Student in RegStudentFile:
      Student=Student.strip()
      Student=Student.split(",")
      print ("\n====================================")
      print("StudentID    :",Student[2])
      print("Full Name    :",Student[3])
      print("Gender       :",Student[4])
      print("E-Mail       :",Student[5])
      print("SportID      :",Student[6])
      print("Sport        :",Student[7])
      print("SportCentreID:",Student[8])
      print("Sport Centre :",Student[9])
   RegStudentFile.close()
def RegStudent_Search():
    Search="y"
    while Search=="y":
        print ("\n====================================\nSearching Registered Students ID Record\n====================================")
        StudentID=input("Enter StudentID: ")
        StudentHandler=open ("Student.txt","r")
        Data=0
        for Student in StudentHandler:
            Student=Student.strip()
            Student=Student.split(",")
            if Student[2]==StudentID:
                print ("\n=========================================")
                print("StudentID    :",Student[2])
                print("Full Name    :",Student[3])
                print("Gender       :",Student[4])
                print("E-Mail       :",Student[5])
                print("SportID      :",Student[6])
                print("Sport        :",Student[7])
                print("SportCentreID:",Student[8])
                print("Sport Centre :",Student[9])
                Data+=1
        StudentHandler.close()
        if Data<1:
            print ("No Specified Student Found")
        else:
            print ("==========================================")
        print(" ")
        Search=input("Do you want to continue searching?(y): ")

def Student_Function():
    Unlogstudent_Interface="y"
    while Unlogstudent_Interface=="y":
        login="false"
        print ("    Command Select:")
        print ("\t1. Login")
        print ("\t2. Register")
        print ("\t3. View Sports Details")
        print ("\t4. View Sports Schedule")
        print ("\t5. Exit")

        try:
           A_choice=int(input("\nEnter Command Choice= "))
        except:
           print ("Invalid Number")
           continue
        if A_choice==1:
            exit="n"
            attempt=0
            login="false"
            while login=="false":
                if exit=="y":
                    print (" ")
                    break
                print (" ")
                Student_Username= input ("Name: ")
                Student_Userpass= input ("Password: ")
                
                Studenthandle=open('Student.txt','r')
                for name in Studenthandle:
                  name=name.strip()
                  name=name.split(",")
                  if (Student_Username, Student_Userpass)==(name[0],name[1]):
                    print ("Succesfully Logged In!")
                    UserData=name
                    Studenthandle.close()
                    login="true"
                    break
                else:
                    print ("Wrong Username/Password")
                    Studenthandle.close()
                    exit=input("Exit Login? (y): ")
                    continue
        elif A_choice==2:
            print(" ")
            Registeration="y"
            while Registeration=="y":
                retry="n"
                Studenthandle=open("Student.txt","r")
                Student_Username=input ("UserName: ")
                for Username in Studenthandle:
                    Username=Username.strip()
                    Username=Username.split(",")
                    if Student_Username == Username[0]:
                        print ("Username not available\n")
                        retry="y"
                if retry=="y":
                    continue
                print ("Username Available\n")
                Studenthandle.close()
                Student_UserPass=input ("Password: ")
                Student_UserPassVer=input ("Re-enter Password: ")
                if Student_UserPass!=Student_UserPassVer:
                    print ("Incorrect Verificaton")
                    continue
                print("Verification Succeed\n")
                Datafilling="y"
                Registeration="n"
                
            while Datafilling=="y":
                BreakCode="n"
                Studenthandle= open("Student.txt","r")
                print("Fill Your Data")
                StudentID=input("StudentID: ")
                for Student in Studenthandle:  
                    Student=Student.strip()
                    Student=Student.split(",")
                    if StudentID==Student[2]:
                        BreakCode="y"
                if BreakCode=="y":
                        print("StudentID Already Used!")
                        continue
                Name=input("Full Name: ")
                Gender=input("Gender: ")
                Email=input("E-Mail: ")
                UserSport=input("Sport: ")
                SportCentre=input("Sport Centre: ")
                SportCentre=SportCentre.replace(" ","")
                Studenthandle.close()
                Sporthandle=open("Sports.txt","r")
                Sporthandle=Sporthandle.readlines()
                checkcounter=0
                for Sport in Sporthandle:
                    Sport=Sport.strip()
                    Sport=Sport.split(",")
                    Sport1=Sport[1]
                    Sport3=Sport[3]
                    Sport1=Sport1.lower()
                    Sport3=Sport3.lower()
                    if (UserSport.lower(),SportCentre.lower())==(Sport1,Sport3):
                        SportID=str(Sport[0])
                        SportCentreID=str(Sport[2])
                        checkcounter+=1
                        break
                if checkcounter!=1:
                    print ("Invalid Sport or Sport Centre")
                    continue
                Studenthandle= open("Student.txt","a")
                Studenthandle.write (Student_Username+","+Student_UserPass+","+StudentID+","+Name+","+Gender+","+Email+","+SportID+","+Sport[1]+","+SportCentreID+","+Sport[3]+","+Sport[4]+"\n")
                Studenthandle.close()
                print("Registration Success\n")
                Datafilling="n"
            
        elif A_choice==3:
                    Sporthandler=open('Sports.txt','r')
                    Sportfile=Sporthandler.readlines()
                    SportSchedulehandler=open ("SportsSchedule.txt","r")
                    SportNum=0
                    for Sport in Sportfile:
                        SC=0
                        Schedule=""
                        Sport= Sport.strip()
                        Sport= Sport.split(",")
                        SportNum+=1
                        if SportNum>1:
                            print ("\n====================================")
                        print("SportID          : ",Sport[0])
                        print("Sport Name       : ",Sport[1])
                        print("Sport Centre Code: ",Sport[2])
                        print("Sport Centre Name: ",Sport[3])
                        print("Sport Fee        : ",Sport[4])
                    Sporthandler.close()
        elif A_choice==4:
            Sporthandle=open("Sports.txt","r")
            Sporthandle=Sporthandle.readlines()
            SC=0
            for Sport in Sporthandle:
                Sport=Sport.strip()
                Sport=Sport.split(",")
                SportID=Sport[0]
                SportCentreID=Sport[2]
                SportSchedulehandler=open ("SportsSchedule.txt","r")
                for Schedule in SportSchedulehandler:
                    Schedule=Schedule.strip()
                    Schedule=Schedule.split(",")
                    if (SportID,SportCentreID)==(Schedule[0],Schedule[1]):
                        SC+=1
                        print ("\t\t====================")
                        print ("\t\tDate: ",Schedule[2])
                        print ("\t\tMonth(Word): ",Schedule[3])
                        print ("\t\tTime: ",Schedule[4])
                        print ("\t\tLocation: ",Schedule[5])
                        print ("\t\tResponsible Coach: ",Schedule[6])
                if SC>1:
                    print ("\t\t====================")
                SportSchedulehandler.close()
        elif A_choice==5:
            Loggedstudent_Interface="n"
            Unlogstudent_Interface="n"
            break
            
        if login=="true":
            Loggedstudent_Interface="y"
            Unlogstudent_Interface="n"
            break
        
        else:
            continue

    while Loggedstudent_Interface=="y":
        
        print("\nWelcome!",Student_Username.strip())
        print ("\n    Command Select:")
        print ("\t1. View Coach Details")
        print ("\t2. View Your Record")
        print ("\t3. View Sport Detail")
        print ("\t4. Modify Self Record")
        print ("\t5. Give feedback and star to Coach")
        print ("\t6. Exit")

        try:
           B_choice=int(input("\nEnter Command Choice= "))
        except:
           print ("Invalid Number")
           continue

        if B_choice==1:
            print ("\n=====================\n    Coach Details\n=====================\n")
            num=1
            Coachfile=open('Coach.txt','r')
            for Coach in Coachfile:
                Coach=Coach.strip()
                Coach=Coach.split(",")
                if num>1:
                    print ("====================")
                print("CoachID           : ",Coach[0])
                print("Name              : ",Coach[1])
                print("Date Joined       : ",Coach[2])
                print("Date Terminated   : ",Coach[3])
                print("Phone Number      : ",Coach[5])
                print("Address           : ",Coach[6])
                print("Sport Centre Code : ",Coach[7])
                print("Sport Centre Name : ",Coach[8])
                print("Sport Code        : ",Coach[9])
                print("Sport Name        : ",Coach[10])
                print("Rating            : ",Coach[11])
                num+=1
            Coachfile.close()
        
        elif B_choice==2:
            print ("\n=====================\n    Your Details\n=====================\n")
            Studenthandle=open('Student.txt','r')
            for Student in Studenthandle:
              Student=Student.strip()
              Student=Student.split(",")
              if (Student_Username, Student_Userpass)==(Student[0],Student[1]):
                print("StudentID    :",Student[2])
                print("Full Name    :",Student[3])
                print("Gender       :",Student[4])
                print("E-Mail       :",Student[5])
                print("SportID      :",Student[6])
                print("Sport        :",Student[7])
                print("SportCentreID:",Student[8])
                print("Sport Centre :",Student[9])
                print("Sport Fee    :",Student[10])
            Studenthandle.close
        

        elif B_choice==3:
            Details="y"
            while Details=="y":
                print ("\n=====================\n    Sport Details\n=====================\n")
                print ("    Choose Which Sport Details to view: ")
                print ("\t1. All Sports Details")
                print ("\t2. Your Sport Details")
                try:
                    C_choice=int(input("Your Choice: "))
                except:
                    print("Invalid Number")
                    continue
                print(" ")
                if C_choice==1:
                    Sporthandler=open('Sports.txt','r')
                    Sportfile=Sporthandler.readlines()
                    SportNum=0
                    for Sport in Sportfile:
                        SC=0
                        Schedule=""
                        Sport= Sport.strip()
                        Sport= Sport.split(",")
                        SportNum+=1
                        if SportNum>1:
                            print ("\n====================================")
                        print("SportID          : ",Sport[0])
                        print("Sport Name       : ",Sport[1])
                        print("Sport Centre Code: ",Sport[2])
                        print("Sport Centre Name: ",Sport[3])
                        print("Sport Fee        : ",Sport[4])
                        print("Schedule         :")
                        SportSchedulehandler=open ("SportsSchedule.txt","r")
                        Schedule=""
                        for Schedule in SportSchedulehandler:
                            Schedule=Schedule.strip()
                            Schedule=Schedule.split(",")
                            if (Sport[0],Sport[2])==(Schedule[0],Schedule[1]):
                                SC+=1
                                print ("\t\t====================")
                                print ("\t\tDate: ",Schedule[2])
                                print ("\t\tMonth(Word): ",Schedule[3])
                                print ("\t\tTime: ",Schedule[4])
                                print ("\t\tLocation: ",Schedule[5])
                                print ("\t\tResponsible Coach: ",Schedule[6])
                        SportSchedulehandler.close()
                        if SC>1:
                            print ("\t\t====================")
                        elif SC==0:
                            print ("\tEMPTY")
                    Sporthandler.close()    
                    Details="n"
                elif C_choice==2:
                    SportSchedulehandler=open ("SportsSchedule.txt","r")
                    Sporthandler=open('Sports.txt','r')
                    Sportfile=Sporthandler.readlines()
                    for Sport in Sportfile:
                        Sport= Sport.strip()
                        Sport= Sport.split(",")
                        SC=0
                        if (Sport[0],Sport[2])==(UserData[6],UserData[8]):
                            print("SportID          : ",Sport[0])
                            print("Sport Name       : ",Sport[1])
                            print("Sport Centre Code: ",Sport[2])
                            print("Sport Centre Name: ",Sport[3])
                            print("Sport Fee        : ",Sport[4])
                            print("Schedule         :")
                            for Schedule in SportSchedulehandler:
                                Schedule=Schedule.strip()
                                Schedule=Schedule.split(",")
                                if (Sport[0],Sport[2])==(Schedule[0],Schedule[1]):
                                    SC+=1
                                    print ("\t\t====================")
                                    print ("\t\tDate: ",Schedule[2])
                                    print ("\t\tMonth(Word): ",Schedule[3])
                                    print ("\t\tTime: ",Schedule[4])
                                    print ("\t\tLocation: ",Schedule[5])
                                    print ("\t\tResponsible Coach: ",Schedule[6])
                        if SC>=1:
                            print ("\t\t====================")
                    SportSchedulehandler.close()
                    Sporthandler.close()
                    Details="n"
                
        elif B_choice==4:
            change="1"
            while change=="1":
                print ("\n=====================\n    Modify Your Details\n=====================\n")
                Studenthandler=open('Student.txt','r')
                Studenthandle=Studenthandler.readlines()
                Studenthandler.close()
                StudentNum=0
                num=1
                for Student in Studenthandle:
                    Student=Student.strip()
                    Student=Student.split(",")
                    StudentNum+=1
                    if (Student_Username, Student_Userpass)==(Student[0],Student[1]):
                        print("[1]StudentID    :",Student[2])
                        print("[2]Full Name    :",Student[3])
                        print("[3]Gender       :",Student[4])
                        print("[4]E-Mail       :",Student[5])
                        print("[5]Sport        :",Student[7])
                        print("[6]Sport Centre :",Student[9])
                        break
                try:
                    Choice=int(input("Select attributes number you wanted to modify: "))
                    if Choice>6 or Choice<1:
                        print ("Number out of range")
                        continue
                    
                except:
                    print("Invalid Number")
                    continue
                
                if Choice==5:
                    N=7
                elif Choice==6:
                    N=9
                else:
                    N=Choice+1
                NewAttr_Val=input("Enter the new data: ")
                print("\nBefore: ",Student[N].strip() )
                print("After: ",NewAttr_Val)
                Confirmation=input("Do you want to proceed the change?(y) :")
                if Confirmation!="y":
                    continue
                S="\n"
                
                if Choice==1:
                    Studenthandle= open("Student.txt","r")
                    for Student in Studenthandle:  
                        Student=Student.strip()
                        Student=Student.split(",")
                        if NewAttr_Val==Student[2]:
                            BreakCode="y"
                    if BreakCode=="y":
                        print("StudentID Already Used!")
                        continue
                    Studenthandler.close()
                elif Choice==5:
                    Sporthandle=open("Sports.txt","r")
                    checkcounter=0
                    NewAttr_Val=NewAttr_Val.replace(" ","")
                    for Sport in Sporthandle:
                        Sport=Sport.strip()
                        Sport=Sport.split(",")
                        SportName=str(Sport[1])
                        SportName=SportName.lower()
                        SportCentreName=str(Sport[3])
                        SportCentreName=SportCentreName.lower()
                        OldCentre=Student[9]
                        OldCentre=OldCentre.lower()
                        if (NewAttr_Val.lower(),OldCentre)==(SportName,SportCentreName):
                            Student[6]=Sport[0]
                            Student[10]=Sport[4]
                            NewAttr_Val=Sport[1]
                            checkcounter+=1
                    Sporthandle.close()
                    if checkcounter>1 or checkcounter<1:
                        print ("Invalid Sport")
                        continue
                elif Choice==6:
                    Sporthandle=open("Sports.txt","r")
                    checkcounter=0
                    NewAttr_Val=NewAttr_Val.replace(" ","")
                    for Sport in Sporthandle:
                        Sport=Sport.strip()
                        Sport=Sport.split(",")
                        SportName=str(Sport[1])
                        SportName=SportName.lower()
                        SportCentreName=str(Sport[3])
                        SportCentreName=SportCentreName.lower()
                        OldSport=Student[7]
                        OldSport=OldSport.lower()
                        if (OldSport,NewAttr_Val.lower())==(SportName,SportCentreName):
                            Student[8]=Sport[2]
                            Student[10]=Sport[4]
                            NewAttr_Val=Sport[3]
                            checkcounter+=1
                    Sporthandle.close()
                    if checkcounter>1 or checkcounter<1:
                        print ("Invalid Sport Centre")
                        continue
                Student[N]=NewAttr_Val
                EditedStudent=",".join(Student)
                Studenthandle[StudentNum-1]=EditedStudent+S

                with open("Student.txt","w") as file:
                    file.writelines(Studenthandle)
                
                Repeat=input("\ndo you want to continue modifying?(y): ")
                if Repeat=="y":
                    continue
                else:
                    change="0"
        elif B_choice==5:
            choice="y"
            while choice=="y":
                Coachhandler=open('Coach.txt','r')
                Coachfile=Coachhandler.readlines()
                CoachNum=0
                print("\n    Choose Couch")
                for Coach in Coachfile:
                    Coach=Coach.strip()
                    Coach=Coach.split(",")
                    print("[",CoachNum+1,"] CoachID:",Coach[0]," Name:",Coach[1])
                    CoachNum+=1
            
                try:
                    Selection=int(input("Enter Couch's Index: "))
                    if Selection>CoachNum or Selection<1:
                        print("Number out of range")
                        continue
                except:
                    print("Invalid Number")
                    continue
                Opinion="y"
                choice="n"
            Selected_Coach=Coachfile[Selection-1].split(",")
            while Opinion=="y":
                try:
                    print("\nRating range from 1-5")
                    Rating=float(input("Enter Rating: "))
                    if Rating>5 or Rating<1:
                        print("Number out of range")
                        continue
                except:
                    print("Invalid Number")
                    continue
                Feedback=input("Enter Feedback: ")
                print ("\nCoachID: ",Selected_Coach[0])
                print("Name: ",Selected_Coach[1])
                print("Feedback: ",Feedback)
                print("Rating: ",Rating)
                Confirmation=input("Give Feedback and Rating to the Coach?(y): ")
                if Confirmation!="y":
                    continue
                else:
                    S="\n"
                    NumFeed=int(Selected_Coach[12])
                    NumFeed=NumFeed+1
                    Totalold=float(Selected_Coach[13])
                    Totalnew=Totalold+Rating
                    Rates=Totalnew/NumFeed
                    Selected_Coach[13]=str(Totalnew)
                    Selected_Coach[12]=str(NumFeed)
                    Selected_Coach[11]=str(Rates)
                    Edited_Coach=",".join(Selected_Coach)
                    Coachfile[Selection-1]=Edited_Coach+S
                    Feedbackfile=open("Feedback.txt","a")
                    Feedbackfile.write(Selected_Coach[0]+","+Feedback+"\n")
                    Feedbackfile.close()
                with open("Coach.txt","w") as file:
                    file.writelines(Coachfile)
                print ("Feedback Given Successfuly")
                Opinion="n"
        if B_choice==6:
            Loggedstudent_Interface="n"
            break



                



        Mchoice=input("\npress enter to return to menu\n")

def Admin_Function():
  login="false"
  while login=="false":
    Admin_username= input ("\nName: ")
    Admin_userpass= input ("Password: ")
    
    Adminhandle=open('Admin.txt','r')
    for name in Adminhandle:
      name=name.strip()
      name=name.split(",")
      if (Admin_username, Admin_userpass)==(name[0],name[1]):
        print ("Admin Verified")
        Adminhandle.close()
        login="true"
        break
    else:
        print ("Wrong Username/Password")
        Adminhandle.close()
        continue

  while login=="true":
    print("\n===========================")
    print ("\tWelcome",Admin_username,"!")
    print ("============================")
    print ("    Command Select:")
    print ("\t1. Add Records")
    print ("\t2. Display Records")
    print ("\t3. Search Records")
    print ("\t4. Sort and display Record")
    print ("\t5. Modify Record")
    print ("\t6. Exit")
    try:
      A_choice=int(input("\nEnter Command Choice= "))
    except:
      print ("Invalid Number")
      continue
    if A_choice==1:
        print("\nAdd Records: \n\t1. Coach\n\t2. Sport\n\t3. Sport Schedule")
        B_choice= input("Enter Choice= ")
        if B_choice=="1":
            Coach_Append()
        elif B_choice=="2":
            Sport_Append()
        elif B_choice=="3":
            SportSchedule_Append()
        else:
            print("Invalid Input")
            continue


    elif A_choice==2:
        print("\nDisplay All Records: \n\t1. Coach\n\t2. Sport\n\t3. Registered Student")
        B_choice= input("Enter Choice= ")
        if B_choice=="1":
            Coach_Display()
        elif B_choice=="2":
            Sport_Display()
        elif B_choice=="3":
            RegStudent_Display()
        else:
            print("Invalid Input")
            continue

          
    elif A_choice==3:
        print("\nSearch Records by: \n\t1. Coach by Coach ID\n\t2. Coach by overall performance (Rating)\n\t3. Sport by Sport ID\n\t4. Student by Student ID")
        B_choice= input("Enter Choice= ")
        if B_choice=="1":
            CoachID_Search()
        elif B_choice=="2":
            CoachRating_Search()
        elif B_choice=="3":
            SportID_Search() 
        elif B_choice=="4":
            RegStudent_Search()
        else:
            print("Invalid Input")
            continue

    elif A_choice==4:
        print("\nSort and Display Coach Records by: \n\t1. Name (Ascending)\n\t2.Hourly Pay Rate (Ascending)\n\t3. Overall Performance (Ascending)")
        B_choice= input("Enter Choice= ")
        if B_choice=="1":
            CoachSort_Name()
        elif B_choice=="2":
            CoachSort_Hourly()
        elif B_choice=="3":
            CoachSort_Performance()
        else:
            print("Invalid Input")
            continue


    elif A_choice==5:
        print("\nModify Records of: \n\t1. Coach\n\t2. Sport\n\t3. Sport Schedule")
        B_choice= input("Enter Choice= ")
        if B_choice=="1":
            ModifyCoach()
        elif B_choice=="2":
            ModifySport()
        elif B_choice=="3":
            ModifySportSchedule()
        else:
            print("Invalid Input")
            continue
    elif A_choice==6:
      break  
    else:
      print ("Invalid Number")
      continue
    MChoice=input ("\nPress enter to return to Admin Menu")
    continue
Identity="False"
program="on"
while program=="on":
    print ("Select Your Identity:\n\n\t1.Admin\n\t2.Students\n\t3.Exit\n")
    while Identity=="False":
        try:
            num=int(input("choice(num): "))
            if num>3 or num<1:
                print ("Number out of range")
                continue
            Identity="True"
        except:
            print("Invalid Choice")
            print(" ")
            continue
        

    while Identity=="True":
        if num==1:
            print ("\n====================\nAdmin Login\n====================\n")
            Admin_Function()
            Identity="False"
            print(" ")
        elif num==2:
            print ("\n====================\nStudent\n====================\n")
            Student_Function()
            Identity="False"
            print (" ")
        elif num==3:
            program="off"
            Identity="False"
        else:
            print("\nnumber's out of range\n")
            Identity="False"     

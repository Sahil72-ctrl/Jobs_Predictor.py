       #--------- Future job Predictor -------#
        #----------- the_kira_x  ---------#
import random
name=(input("what is your name ?"))
print(name, "let me look at your prediction")

while True:
    print("1. IT and Software Development")
    print("2. Healthcare and Life science")
    print("3. Enginnering and Manufacturing")
    print("4. Arts and Design")

    choose=(input("choose a number from (1-4):"))
    choose=choose.strip()
    print("\n")

    if choose == "1":
        print("1. Front End & Back End Developer")
        print("2. Mobile app Developer")
        print("3. Software Engineer")
        print("4. Network Administrator")
        print("\n")
        break
    
    elif choose == "2":
        print("5. Laboratory Technician")
        print("6. Research Assistant")
        print("7. medical coder")
        print("8. healthcare analytics")
        print("\n")
        break
    
    elif choose == "3":
        print("9. Production Engineer")
        print("10. Design Engineer")
        print("11. Prototype Engineer")
        print("12. Service Engineer")
        print("\n")
        break
    
    elif choose == "4":
        print("13. Graphic Designer")
        print("14. Fashion Designer")
        print("15. Motion Graphics Artist")
        print("16. Web Designer")
        print("\n")
        break
    
else:
    print("wrong option! try again:")
    
while True:

    print("let Me See Your Fate Now")
    print("1. Check Automatic Fate")
    print("2. I Dont Need Predictions")
    option=input("Choose An Option (1-2):")
    
    
    random_number=random.randint(0,16)
   
    if option == "1":
        print(name ,random_number , "Is Your Fate Number")
    
    elif option == "2":
        print("No Problem Still Thanku")
    else:
        print ("wrong input try again")   

    if random_number == 0:
      print(name , "your fate job is: Web Designer Congrats")
      break
    elif random_number == 1:   
      print(name , "your fate job is: Fashion Designer Congrats")
      break
    elif random_number == 2:
      print(name, "your fate job is: Service Engineer Congrats")
      break
    elif random_number == 3:
      print(name, "your fate job is: Design Engineer Congrats")
      break
    elif random_number == 4:
      print(name, "your fate job is: Healthcare Analytics Congrats")
      break
    elif random_number == 5:
      print(name, "your fate job is: Research Assistant Congrats")
      break
    elif random_number == 6:
      print(name, "your fate job is: Network Administrator Congrats ")
      break
    elif random_number == 7:
      print(name, "your fate job is: Mobile App Developer Congrats")
      break
    elif random_number == 8:
      print(name, "your fate job is: Front End And Back End Developer Congrats")
      break
    elif random_number == 9:
      print(name , "your fate job is: Software Engineer Congrats")
      break
    elif random_number == 10:
      print(name, "your fate job is: Laboratory Technician Congrats")
      break    
    elif random_number == 11:
      print(name, "your fate job is: Medical Coder Congrats")
      break
    elif random_number == 12:
      print(name, "your fate job is: Production Engineer Congrats")
      break
    elif random_number == 13:
      print(name, "your fate job is: Prototype Engineer Congrats")
      break
    elif random_number == 14:
      print(name, "your fate job is: Graphic Designer Congrats")
      break
    elif random_number == 15:
      print(name, "your fate job is: Motion Graphic Artist Congrats")
      break
    elif random_number == 16:
      print(name, "your fate job is: Jobless!!!")
      break
      ("\n")
    
    else:
      print("wrong input try again")
      
      
follow=input("have you followed me on insta ? , (yes-no):")
follow=follow.strip()
if follow=="yes":
    print(name, "thnks alot buddy")
elif follow=="no":
    print(name, "the_kira_x , follow me on insta")

      


#while choose >=1:
    #print("correct")
#else:
   # print("wrong input! try again")
    #choose=int(input("type a number from (1-4):"))
#if choose =     
#try:
    #choice = int(input("\nEnter your choice (1-4): "))
#except:
   # print(" invalid input! please run again.")
   # exit()
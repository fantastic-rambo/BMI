print("Hello! Welcome to the BMI Tracking app! \n")
print("==================================================")

   #input functionality

while True:
    name = input("Please enter your name: ").upper()
    age = int(input("How old are you?: "))
    print("Please enter your weight in kilograms.")
    weight = float(input("How much do you weigh?: "))
    print("Please enter your height in meters.")
    height = float(input("What's your height?: "))

    # calculating for the BMI
    
    BMI = round(weight / height ** 2, 1)

    print("==================================================")

# logic

    if BMI <= 18.4:
        print("Name:", name, "\nAge:", age, "\nWeight:", weight,"kg",
          "\nHeight:", height,"m", "\nBMI:", BMI, "\nStatus: Underweight", "\nAdvice: Please eat more.")

    elif BMI > 18.4 and BMI <= 24.9:
        print("Name:", name, "\nAge:", age, "\nWeight:", weight,"kg",
          "\nHeight:", height,"m", "\nBMI:", BMI, "\nStatus: Normal", "\nAdvice: You are fit. Keep it up!" )

    elif BMI > 24.9 and BMI <= 39.9:
        print("Name:", name, "\nAge:", age, "\nWeight:", weight,"kg", "\nHeight:", height,"m",
          "\nBMI:", BMI, "\nStatus: Overweight", "\nAdvice: You'd have to check your food intake and exercise some more.")
    else:
        print("Name:", name, "\nAge:", age, "\nWeight:", weight,"kg", "\nHeight:", height,"m",
          "\nBMI:", BMI, "\nStatus: Obese", "\nAdvice: Please visit your doctor immediately." )

        print("\n==================================================")
        
#Prompt user to calculate another BMI

    restart = input("Do you want to restart the process? (y/n): ")

    if restart == "y":
        continue
    
#Allow user to exit app

    elif restart == "n":

        print("\n==================================================")

        print("Thank you for using the app \n Powered by PAARN")
        exit()
    else:
        print("Invalid input. Please enter (y/n):")
        
    

   


    

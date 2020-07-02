totalPoints = 0

totalUnits = 0

cntCourses = 0

def display():

  print("1. Enter course grade and units.")

  print("2. Show GPA.")

  print("3. Quit.")

  print("Enter your choice")

  choice = input()    #Taking choice as input from user

  if(choice == '1' or choice == '2' or choice == '3'):

    return int(choice)

  else:

    print("Invalid Choice")     #If user makes an invalid choice

    return -1

def legal(amount, lowerBound, upperBound):

  if amount >= lowerBound and amount <= upperBound:

    return True

  else:

    return False

def main():

  global totalUnits, totalPoints, cntCourses

  choice = display()

  

  if choice == 1:

    print("Enter grade for your course")

    grade = int(input())

    print("Enter units for your course")

    units = int(input())

    if legal(grade, 0, 4) and legal(units, 1, 5):

      totalPoints += grade*units

      totalUnits += units

      cntCourses += 1

    else:

      print("Grade or units is of invalid range")

    print()   #For a line break

    main()  #Recursively calling main

  elif choice == 2:

    if totalUnits != 0:

      GPA = totalPoints/totalUnits

    else:

      GPA = 0

    print("Current GPA : ", GPA)

    print()   #For a line break

    main()  #Recursively calling main

  

  elif choice == 3:

    print("Number of Courses Taken : ", cntCourses)   #Number of courses taken by user

    print("Good bye !!!")

  

  else:   #For invalid choice

    print()   #For a line break

    main()    #Again letting user to make choice

main()
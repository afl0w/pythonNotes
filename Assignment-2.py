
def convertTemperature(tempF):
   """ Function that converts Fahrenheit to Celsius """
   # Converting temperature
   tempC = (tempF - 32) / 1.8
   return tempC
  # Converting speed
def convertSpeed(speedMHr):
   """ Function that converts Spped from Miles Per Hour to Meters Per Second """
   speedMSec = speedMHr / 2.237
   return speedMSec
  
def processOfdata():
   """ Main Function """
   print("Enter 1 to convert Fahrenheit from temperature to Celsius: ")
   print("Enter 2 to convert Speed in Miles/Hour to Meters/Second: ")
   # Reading MainIP aka main input
   mainIP = int(input("Enter your choice (1 or 2): "))
   # Checking main input
   if mainIP == 1:
       # Reading temperature
       tempF = float(input("Enter temperature in Fahrenheit: "))
       # Converting to Celsius
       tempC = convertTemperature(tempF)
       # Printing result
       print("Temperature in Celsius: " + str(tempC))
   elif mainIP == 2:
       # Reading Speed
       speedMHr = float(input("Enter Speed in Miles/Hour: "))
       # Converting to Meters/Second
       speedMSec = convertTemperature(speedMHr)
       # Printing result
       print("Speed in Meters/Second: " + str(speedMSec))
   else:
       print("Invalid Option entered...")
      
# Calling main function
processOfdata()
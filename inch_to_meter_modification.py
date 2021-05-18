#inch_to_meter_modification.py
#This program will convert inches to either meters or centimeters depending on if the inches is greater or less than 100
#Justin Middagh
#Hilbert College - CS131
#September 20,2020

def main():
#the line abouve defines the function that will be created, named main        
	inches = int(input("Enter the number in inches to be converted to meters: ")) 
#the line above takes a value (int) as input to be used in the conversion below
	meters = inches * 0.0254	
	centimeters = inches * 2.54
#the lines above are the mathematical operations to be performed on the conversions	
	if inches > 100:
            print(inches,"inches converts to",meters,"meters")
	else:
    		print(inches,"inches converts to",centimeters,"centimeters")
#the lines above are an if/else statement that determines if the input is greater than 100; then prints the appropriate print statement
#the else statment will print the conversion should the original int input be less than 100
main()

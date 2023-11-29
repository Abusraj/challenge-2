
import random;
def main ( ) :
    number = RandomNumber ()
    guess =input ("Enter a number")
    result=CheckUserChoice(number ,guess)
    if(result):
        print("Correct")
    else:
        print("Wrong")
        
    return None
def RandomNumber():
    return random.randrange(1,10)
def CheckUserChoice (number,guess):
    return (number==guess)
main()
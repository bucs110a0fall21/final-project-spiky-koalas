
#import your controller
import pygame

def main():
    pygame.init()
    team = {"lead": "Madeline Scotti", "backend": "Luisa Urgiles", "frontend": "Klara Veljkovic"}
    print("Software Lead is:", team["lead"])
    print("Backend is:", team["backend"])
    print("Frontend is:" , team["frontend"])
    #Create an instance on your controller objects
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 2 LINES OF CODE ######
main()

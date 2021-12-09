:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# The Haunted Mansion
## CS 110 Final Project
### Fall 2021
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)

<< [https://github.com/<repo>](#) >>

<< [https://docs.google.com/presentation/d/1OxxwIGcMleXSVdTLxSrG6W3KtX3ggaaaX9cc-2JWcY0/edit?usp=sharing] >>

<<<<<<< HEAD
### Team: Spiky Koalas
#### Madeline Scotti, Klara Veljkovic, Luisa Urgiles
=======
### Team: Spiky Koalas 
#### Madeline Scotti, Klara Veljkovic, Luisa Urgiles
>>>>>>> 98ea08ac1992bec57d62a2a085ad75f0a9c1427a

***

## Project Description *(Software Lead)*
  
Basic RPG game. Has a menu page that allows you to either start a new game and enter your name, load an existing saved game using a save file, or exit/quit the game. After the game starts, the "Player" is put inside of the mansion and will see a book, potion, and 1 enemy. The user can use the arrow keys to move the Player and the space bar to attack. If the Player collides with and attacks the enemy, the enemy's health will decrese, but if the Player is not attacking then the Player will lose health. Anytime during the game, if the player collides with the book, then the player will be able to save the game and then coninue or save the game and quit to the menu screen. If the player collides with the potion their health will be brought back to full health (100). If the enemy looses all of its health, then the player wins and the screen will change to display "Enemey Defeated" and give the user an option to exit to menu. If the player looses all of their health, then the screen will change to display "Game Over" and the user will have the option to quit the game or reload from save point. 

***    

## User Interface Design *(Front End Specialist)*
Start page drawing.
![Start Page](https://user-images.githubusercontent.com/89892102/145114765-0323b71a-0cc5-439a-871d-b951caf820d2.png)
^ The start page contains the "Start game"-Begins the game when pressed,, "Load game"-Loads the save file, "Exit"-Will exit the program. Has a small picture relating to the game concept.
   
Game screen drawing.
![game screen](https://user-images.githubusercontent.com/89892102/145115320-a44df99a-7890-4031-9b73-082f2e93bce8.png)
^ Has the character, enemy, and object on the screen with a background. Object should be interactable and the enemy should be able to be removed from the screen when killed.
  
Pick up book in game screen (Save screen).
![Pause screen (1)](https://user-images.githubusercontent.com/89892102/145122945-5c06478f-2cbc-4336-bd77-ad3ffdcf26e0.png)
^ Has 3 options for the player to pick when they pick up the book. Each button does as it says.
   
Game over drawing.
![Game over](https://user-images.githubusercontent.com/89892102/145115554-8caac79f-2d08-4d0f-8e38-9d8a05afa75e.png)
^ Game over screen should have a "Try again"-Changes the screen back to the Start page/Main Menu and "Exit"-Exits the program, button.
  
Victory screen.
![Victory screen](https://user-images.githubusercontent.com/89892102/145123039-70109e9f-00e2-4c48-856d-14c9d0aaa5a3.png)
^ Screen is displayed after enemy is defeated and player picks up an item. Text should say victory, etc. Player can only now exit the game.

Final GUI!!!
![Screen Shot 2021-12-07 at 6 20 24 PM](https://user-images.githubusercontent.com/89892102/145317504-bde0ee9c-88fd-45e8-bad5-a48a4edd455d.png)
![Screen Shot 2021-12-08 at 8 24 03 PM](https://user-images.githubusercontent.com/89892102/145317511-46a0ae21-175a-4902-8f49-e5c1f4fe157b.png)
![Screen Shot 2021-12-08 at 7 31 50 PM](https://user-images.githubusercontent.com/89892102/145317520-e790ac13-76b9-426a-97b8-eb392cf9e182.png)
![Screen Shot 2021-12-08 at 6 49 12 PM](https://user-images.githubusercontent.com/89892102/145317524-4ba450be-5291-4856-9e93-6b840f26303e.png)
![Screen Shot 2021-12-08 at 7 31 31 PM](https://user-images.githubusercontent.com/89892102/145317530-22462d65-baa1-46d8-8322-99a5a2b6dbf2.png)


***        

## Program Design *(Backend Specialist)*
* Non-Standard libraries
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. >>
    * For each additional module you should include
        * url for the module documentation
        * a short description of the module
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). >>
        * ![class diagram](assets/class_diagram.jpg)
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* Classes
    * << You should have a list of each of your classes with a description. >>

## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:
* main.py
* bin
    <all of your python files should go here>
    * Controller.py
    * Player.py
    * Enemy.py
    * Item.py
* assets
    * <all of your media, i.e. images, font files, etc, should go here)>
<<<<<<< HEAD
=======
Images.
![Book](https://user-images.githubusercontent.com/89892102/145116243-ae598475-24ff-4240-a590-f52dce61703f.png)
![button](https://user-images.githubusercontent.com/89892102/145116258-fdbe39c7-9002-4d1a-9806-2282da7664cb.png)
![enemy_L](https://user-images.githubusercontent.com/89892102/145116283-0ac7df26-e451-4e53-bb0f-16455a3fa9d4.png)
![gameover](https://user-images.githubusercontent.com/89892102/145116308-ee2d190b-3e56-4c23-972f-01783105f562.png)
![inside_mw](https://user-images.githubusercontent.com/89892102/145116325-f5ef6e27-7533-49af-a4e8-94221710561a.png)
![mansion](https://user-images.githubusercontent.com/89892102/145116481-a190b0e6-582e-4ec8-bac5-b2857f8d9992.png)
![Player_U](https://user-images.githubusercontent.com/89892102/145123210-ab78206f-2155-4206-9efa-6721fa1aec3b.png)
![Player_RA2](https://user-images.githubusercontent.com/89892102/145123215-cbfbc93f-150a-453a-8e7e-8b556be162e4.png)
![Player_RA1](https://user-images.githubusercontent.com/89892102/145123226-682aec8b-c9ad-437e-a958-8bbe53485770.png)
![Player_LA2](https://user-images.githubusercontent.com/89892102/145123233-301e56dd-3942-4d08-8d21-cb75a37f499a.png)
![Player_LA1](https://user-images.githubusercontent.com/89892102/145123240-89c71fbb-2cae-4a28-b36a-c3213ff29ac1.png)
![Player_L](https://user-images.githubusercontent.com/89892102/145123247-371b4ba3-ad08-40e0-aacd-437083de8210.png)
![Player_D](https://user-images.githubusercontent.com/89892102/145123254-728c767d-569a-4e09-9f96-0ea9a669adc6.png)
![Player_R](https://user-images.githubusercontent.com/89892102/145123319-3d6807b1-501f-487c-b4c3-11317f0323b8.png)
![trophy](https://user-images.githubusercontent.com/89892102/145312600-f4fd659b-a73b-43ab-bfaa-03e5aa62207b.png)
![balloons](https://user-images.githubusercontent.com/89892102/145312602-3652397f-5218-4d00-bc83-419c621fefd8.png)

           
Fonts (Preview).
![PREVIEW DAFONT DIN STD](https://user-images.githubusercontent.com/89892102/145116378-91d962e5-e489-41ab-8551-cf5c032b2318.png)
![Stranger Cover](https://user-images.githubusercontent.com/89892102/145116437-b0a493df-3639-4bc5-80a5-0874dc24e5c3.PNG)
      
<<<<<<< HEAD
>>>>>>> 675ccfb5f1a555f57c422dcda63f8037d48cbdf7
=======
             [Project Structure (1).pdf](https://github.com/bucs110a0fall21/final-project-spiky-koalas/files/7500290/Project.Structure.1.pdf)
>>>>>>> 98ea08ac1992bec57d62a2a085ad75f0a9c1427a

* etc
    * <This is a catch all folder for things that are not part of your project, but you want to keep with your project. Your demo video should go here.>

***

## Tasks and Responsibilities *(Software Lead)*
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - Madeline Scotti
Worked as integration specialist by
       Did most of pixel art and GUI designing
       Colloborated on/helped write Controller, Enemy, Item and Hero classes
       Gave ideas on how to structure code and what to fix in Controller, Enemy, and Hero classes

### Front End Specialist - Klara Veljkovic
Front-end lead conducted significant research on
       Controller class 
       GUI

### Back End Specialist - Luisa Urgiles
The back end specialist
      Enemy class
      Player Class
      Item Class
      Collaborated with the GUI
      
## Testing *(Software Lead)*
      Ran the code repeatedly whenever an error came up until it could be specifically identified. Then fixed issues and ran code again trying to cause the same error from before to see if problem was actuallly fixed. For example, When the backspace feature when typing in the inpuit box on the menu page did not work. We tried to run the code over an over to see exactly what the problem was. Also, asked Prof. Moore for help. Then after finding the issue and fixing it, we ran the menu page many times trying to get an error, such as writing more code than the amount of space in the box, writing letters that go below the box line a little, ie. gpq, etc and seeing if the backspace still worked. We also had UX becuase we had our friends test our code
      

* Your ATP
   
   https://docs.google.com/document/d/1QgSzXg7QFyQTuhldvFxYSisDCKwrF7AnpJ15ZKLmcSE/edit?usp=sharing

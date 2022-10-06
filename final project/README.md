# Random Guessing Game
#### Video Demo:  https://www.youtube.com/watch?v=0Sa_eZPbJLw
#### Description:

##### I tried improving "game.py" made in CS50P stored in the "game" folder. Introducing the usage of lives using classes, and the "art" library.

##### The "project.py" starts with a Class named "Points" which is used to store the lives of the player (the lives are randomized between 5 to 10).

##### Then there's the main function that has a while loop that will not stop untill there's lives left.

##### We have the get_guess function that is called by main and return the guess inserted.

##### After that the check function is called which receives the random number and the guess. It returns a ASCII TEXT and the remaining lives (by calling the new_lives function) if the guess is higher or lower than the randomized number. Or it stops the loop and congratulates the player.

##### The new_lives function when called reduces the lives from the Points class and if the lives reach 0, Game Over is returned.

##### Most of the error handling is made inside of the project itself with try and except. The test_project file could not be used too well because most of the functions interact with each other from the start of the program.

##### In the test_project its used 'monkeypatch', it helps to set the input from the get_guess function in what I desire it to be.

##### The 'art' library can import various types of ascii art, I decided to use the "small" for the convenience of it being easier to read, as seen in the main project, all the printing is made using art.tprint() that prints the text inside in ASCII ART.

##### I tried making the code as easy to read as possible, putting everything inside its own functions. Just some variables are made outside for the sake of it being global.
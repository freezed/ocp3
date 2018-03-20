-[_Open Classrooms courses_](https://openclassrooms.com/projects/aidez-macgyver-a-sechapper)-

# [PyDev] Project 3

#### Help McGyver to escape!

----

### Summary

Imagine a 2D labyrinth in which _McGyver_ would have been locked up.
The exit is watched over by a bodyguard. To distract him, you need to
combine the following elements dispersed in the labyrinth:

* a needle
* a small plastic tube
* ether

They'll allow _McGyver_ to create a syringe and put our guard asleep.


### Features

* One level. The structure (departure, location of the walls, arrival),
should be saved in a file to easily modify it if necessary.
* _McGyver_ will be controlled by the directional keys on the keyboard.
* The objects will be randomly distributed in the maze and will change
locations if the user closes the game and raises it.
* The game window will be a square of 15 sprites length.
* _McGyver_ will have to move from square to square, with 15 squares along
the window's length
* It will retrieve an object simply by moving on it.
* The program stops only if _McGyver_ has recovered all objects and found
the exit from the maze. If he stupid enough to comes in front of the the
guard without all the objects, he dies (according to the evolution theory).
* The program will be standalone, i. e. it can be run on any computer.

### Steps

1. Create the starting frame
    * [x] Initialize a Git repo on Github
    * [x] Create the labyrinth without the graphical user interface
    * [ ] Start the graphical interface with PyGame
    * [ ] Represent the guard, _McGyver_ and the objects in your program
    and placed them at the beginning of the game
2. Animate the character
    * [ ] The only moving element is _McGyver_, create classes methods for
    animation and finding the exit
    * [ ] make a simplified version of the game in which _McGyver_ wins
    when he arrives in front of the goalkeeper
3. Recovering objects
    * [ ] Add object management
    * [ ] The way he pick them up
    * [ ] Add a counter that will list them.
4. Win!
    * [ ] _McGyver_ has picked up all the objects and asleep the guard

### Deliverables

* program hosted by Github
* 2 pages text doc (pdf) explaining your approach:
    * including the link to your repo
    * develop the choice of algorithm
    * explain the difficulties encountered and the solutions found

### Constraints

* version your code and publish it on Github
* follow the good practices of PEP 8
* develop in a virtual environment using Python 3
* code must be written in English
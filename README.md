-[_Open Classrooms courses_](https://openclassrooms.com/projects/aidez-macgyver-a-sechapper)-

# [PyDev] Projet 3

#### Help MacGyver to escape!

----

### Summary

Imagine a 2D labyrinth in which _[MacGyver](https://en.wikipedia.org/wiki/MacGyver_(1985_TV_series))_ would have been locked up.
The exit is watched over by a bodyguard. To distract him, you need to
combine the following elements dispersed in the labyrinth:

* a needle
* a tube
* ether

They'll allow _MacGyver_ to create a syringe and put our guard asleep.

### Usage

This have been made with `python 3.6.4` and `pygame 1.9.3`

#### On Linux

1. Clone repo: `git clone https://github.com/freezed/ocp3`
2. Install dependences: `cd ocp3; pip3 install -r requirement.txt`
3. Run it: `python3 main.py`

#### Other OS

Feel free to contribute, I do not use other OS

### Files

* `main.py`, main script the one to run
* `conf.py`, place for variables, constants and fuctions
* `maze.py`, Maze class
* `player.py`, Player class
* `gui.py`, GraphicUI class
* `01.maze`, maze file
* `img/`, directory for image files
* `requirement.txt`, dependences for feeding pip
* `README.md`, you're reading it!

### Features

* One level. The structure (departure, location of the walls, arrival),
should be saved in a file to easily modify it if necessary.
* _MacGyver_ will be controlled by the directional keys on the keyboard.
* The objects will be randomly distributed in the maze and will change
locations if the user closes the game and raises it.
* The game window will be a square of 15 sprites length.
* _MacGyver_ will have to move from square to square, with 15 squares along
the window's length
* It will retrieve an object simply by moving on it.
* The program stops only if _MacGyver_ has recovered all objects and found
the exit from the maze. If he stupid enough to comes in front of the the
guard without all the objects, he dies (according to the evolution theory).
* The program will be standalone, i. e. it can be run on any computer.

### Roadmaze

1. Create the starting frame
    * [x] Initialize a Git repo on Github
    * [x] Create the labyrinth without the graphical user interface
    * [x] Start the graphical interface with PyGame
    * [x] Represent the guard, _MacGyver_ and the objects in your program
    and placed them at the beginning of the game
2. Animate the character
    * [x] The only moving element is _MacGyver_, create classes methods for
    animation and finding the exit
    * [x] make a simplified version of the game in which _MacGyver_ wins
    when he arrives in front of the goalkeeper
3. Recovering objects
    * [x] Add object management
    * [x] The way he pick them up
    * [x] Add a counter that will list them.
4. Win!
    * [x] _MacGyver_ has picked up all the objects and asleep the guard

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

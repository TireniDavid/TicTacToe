# TicTacToe
In this project, we'll develop an interactive, user-friendly TicTacToe game that can be played between two players. It's an excellent opportunity to enhance our programming skills and gain practical experience in applying coding concepts.

**Game Board Data Structures**: 

To design the game board for a TicTacToe game, we could use a 2D ARRAY list of list . 

**Players:** 

Two  (Player and Computer)

**Player Input 1( can either choose X or O)**:

if player USER chooses X, Computer would be forced to use O,  player must use this throughout the game.

, or if player USER chooses O, Computer would be forced to use X,  player must use this throughout the game.

players cannot choose anything other than X or O

      *Invalid Input Handling 1:*

If the player chooses an invalid input (anything other than X or O), the game should continue to prompt the player for correct input until a valid choice is made.

**Player Input2 (choose position on the grid)** :

players can only choose from 0 to 8: a list from: (1 to 8)

when any of this number is chosen, the next player can no longer choose such option, so it is popped out of the list.

[ [ 0 ]     [ 1 ]     [ 2 ] ]

[ [ 3 ]     [ 4 ]     [ 5 ] ]

[ [ 6 ]     [ 7 ]     [ 8 ] ] 

players cannot choose any integer less than 0 or greater than 8. 

     *Invalid Input Handling 2:* 

If the player chooses an invalid input (any integer less than 0 or greater than 8), the game should continue to prompt the player for correct input until a valid choice is made. 

**Both Player’s input1 & 2 makes a TUPLE (Input1 , Input2)**

for example player chooses (X, 0). then 0 is removed from the list of (0 to 8), which becomes (1 to 8 ). then computer have to go with O (O, 3), then 3 must be removed from the list and you left with (1 to 2 & 4 to 8) 

[ [ X ]    [ 1 ]     [ 2 ] ]

[ [ O]    [ 4 ]     [ 5 ] ]

[ [ 6 ]    [ 7 ]     [ 8 ] ] 

**Draw Situation (Player & Computer )**: All 8 numbers have been used and Still No **Win!** 

**Win Situation(Computer or Player):**

Win Possibilities: (0,1,2) or (3, 4, 5) or (6, 7, 8) or (0,3,6) or (1, 4, 7) or (2, 5, 8) or (2, 4, 6) or (0, 4, 8)

If and only if any of the Win Possibilities are found in the Player’s or Computer’s position Catalog, then the **Player or Computer** Win. For example, if  the player chose(0, 4, 7, 1) sorted(0, 1, 4, 7). Since (1, 4, 7) is a subset of the **Player’s or Computer’s** Catalog, A Win is Declared.

If subset is found in **Player’**s Catalog, then **Playe**r wins.

If subset is found in **Computer**’s Catalog, then **Computer** wins.

**Lose** (**Computer or Player**): 

If Player Wins, then Computer Loses. (You Won!)

If Computer Wins, then Player Loses. (You Lost!) 

Win Strategy (0 (1) (2) (3) (5)  (6 ) ( ) )


  CIVIL WAR
 ============

time limit per test: 1 second
memory limit per test: 
256 megabytes
input: standard input
output: standard output



Once, there arose a dispute between Captain America and Iron Man. To solve the dispute, they decided to play an intellectual game.

The game is played on a circular table where 2N+1 cards are placed with numbers print on only one side of the card from 1 to 2N+1 sequentially. Initially all cards are flipped such that number is on the other side of every card. The game goes as follow –

1.Iron Man starts and on his move he can turn any card straight so that number comes in the visible side.

2.Captain on his move can flip back at most one card that is adjacent to the card that Iron Man turned just now straight.

3.Note – Captain cannot turn a card straight; he can only turn them back.

Iron Man wins if at any moment there are  K  cards showing their number after Captain has made his move. As Iron man has some urgent work he wants to end the game as soon as possible and just from the value of  N  and  K  Iron Man can decide whether he can surely win the game or not, and if he can win for sure he will play the sequence of move which completes the game in least possible moves. Also even if Captain knows he cannot win the game he will move the best possible move available so he can delay the game.

You are given  N  and  K, your work is to tell whether Iron Man can win the game or not. If he can, print  W  the minimum number of moves required to win the game. Let P is a set formed by those  K  numbers which are visible after W moves (when Iron Man has win). Your task is to print number of all possible distinct set P.

## Input

The first line contains the integer $t$ $(1 ≤ t ≤ 10^5)$— the number of test cases.

The single line of each test case contains the integer  $n$ $(1 < n ≤ 5×10^5)$ and  $k$ $(1 ≤ k ≤ 2n+1)$.

## Output

If Iron Man can win the game: First line consists of "Yes" and next line contain of two space separated integer  W  and  X  where  W  is the minimum number of moves required to win the game and  X  is no. of distinct possible sets of P.

Else print "No".

As value of X can go very large print X mod  10^9^+7.


## Example

| Input                                                 | 
|-------------------------------------------------------|
| 8 |
|  3 1|
|4 9|
|	2 3|
|	8 2|
|	6 6|
|	2 1|
|	1000 1000|
|	12345 6789|                                                     

| Output |
| -----|
|Yes |
| 1 7 |
|No|
|Yes|
|4 5|
|Yes|
|2 119|
|Yes|
|6 13|
|Yes|
|1 5|
|Yes|
|1000 2001|
|Yes|
|6789 855379062|


## Note
In first test case $n=3$ and $k=1$ so there are 7 cards around the table and if Iron Man turns any of the card he will win as Captain has no option to turn back a card so least moves is 1 while he can turn any of the 7 card so possible set is {1} , {2} , {3} ... {7}.

In second test case there is no possible way to win the match.

In third test case $n=2$ and $k=3$ here there are 5 cards in the table [1,2,3,4,5] where next to 5 is 1 , now possible sequence of moves for Iron Man to win in least moves(0 represents Captain doesn't turn any card)   $I=1,C=0,I=3,C=0,I=2,C=1,I=5,C=0$ or $I=3,C=0,I=5,C=0,I=4,C=3,I=2,C=0$ having set P = {2,3,5} and  {2,4,5} respectively and other possible sequence will give {1,3,4} , {1,2,4} and {1,3,5}.It can be checked that no other possible set P is available. So minimum moves required is 4 and all possible set P are 5.


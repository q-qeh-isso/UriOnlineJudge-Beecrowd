# The Coins of Robbie

---

Robbie is a robot very charismatic, and one of things that he most like to do, besides playing with Glória, it's collect coins. Robbie has several coins with equal or different values, and the same size. They’re stored in na organize manner on top of each other, inside a glass cylinder. Robbie Always do a little game with Glória using his coins when she ask to play with him from hide and seek, or when she asks him to take her for a walk. The rule of the game is: Glória have to choose any number **N**, which will be added, then for each coin **N** the value of the coin **Vi** is added until there aren’t no more coins, in other words Ʃ of ((**V****M**-(**N***0) )+(**V****M**-(**N***1))+(**V****M**-(**N***2))...), M it’s the number of coins. For exemple, if there’re 5 coins with values 1, 2, 3, 4 and 5, and Glória choose 2 as a number of jump, them the coins will be added 5, 3 and 1, result in 9. In the end, Robbie checks if the sum of these coins is a prime number, if this happen, he do what Glória want, if doesn’t happen, the little girl convince Robbie to play again, Cause she Always convince him to do everything, saying 
that will stop to tell him stories, if he doesn’t make her wish.

You as a good developer of U.S Robots, will help this two friends, writting a computer program that will say the result of the game.

## Input

The input contains several test cases. The first line of a test case contains an integer **M** (2 ≤ **M** ≤ 20) that represents the quantity of coins. Each of the next lines **M** contains an integer **Vi** (1 ≤ **Vi** ≤500) that represents the value of coins **Mi** , and for the last one, a integer **N** (1 ≤ **N** ≤ **M**) that’s the jump in the added choosen by Gloria.

The input ends with EOF.

## Output

Print “You’re a coastal aircraft, Robbie, a large silver aircraft.”, if Gloria win the game, or “Bad boy! I’ll hit you.”, if Glória loose the game. The output should be no quotation marks.

| Input Sample                                                                                                    | Output Sample                                                                           |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| 5<br><br>1<br><br>2<br><br>3<br><br>4<br><br>5<br><br>2 5<br><br>1<br><br>2<br><br>3<br><br>4<br><br>5<br><br>3 | Bad boy! I’ll hit you. <br/>You’re a coastal aircraft, Robbie, a large silver aircraft. |

[beecrowd](https://www.beecrowd.com.br/judge/en/problems/view/2709)

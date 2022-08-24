# The Return of The King

---

Frodo and Sam are about to throw the ring on the Mountain of Perdition, but Gollum disturbs them.  
**A little pause in history.** Lord of the Rings, besides being one of humanity's greatest literary and cinematographic classics, is a story that makes clear the value of friendship. Give value to good friendships :) **Resume.**  
Gollum is an unhappy and unbearable being. For Frodo and Sam to get through it, they need to recite runes that sing friendship. Each rune is represented by a letter of the alphabet, and indicates a quantity of friendship that it emits, being able to be positive or negative (yes, there are runes that represent the most friendships).  
Given the amount of friendship necessary to defeat Gollum, a list of runes and their respective values ​​of friendship, and the runes that Sam and Frodo recited, give the ultimate worth of friendship that Frodo and Sam succeeded in and whether or not it was possible to defeat Gollum.

## Input

The first line of the entry consists of two integers **N**(1 <= **N**) and **G**(**G** <= 100), indicating, respectively, the number of runes in existence, and the amount of friendship necessary to defeat Gollum. The next N lines are composed of a character **Ri**('A' <= **Ri** <= 'Z') and an integer **Vi**(-100 <= **Vi** <= 100), indicating, respectively, the rune and the value of 
friendship that it adds. The next line is started by an integer **X**, indicating the number of runes recited by Frodo and Sam. The last line of the entry is composed of X characters, indicating the runes recited by Frodo and Sam.

## Output

The first line of the output should contain the amount of friendship value. The second line should contain one of the following messages:  
● "My precioooous", if Gollum wins;  
● "You shall pass!" If Frodo and Sam win.

| Input Sample                                                                                                                   | Output Sample             |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------- |
| 8 10<br><br>D 5<br><br>B 5<br><br>V 5<br><br>A -10<br><br>X -2<br><br>S -4<br><br>J 5<br><br>R 5<br><br>5<br><br>D A B V R<br> | 10<br><br>You shall pass! |

[beecrowd](https://www.beecrowd.com.br/judge/en/problems/view/2951)

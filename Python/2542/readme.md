# Iu-Di-Oh!

---

*Iu-di-oh!* is a card game really popular among kids! Every *Iu-di-oh!* player has his own deck containing many cards. Each card contains **N** attributes (such as power, speed, smartness, etc.). Attributes are numbered from 1 to **N** and are given as positive integers.

A match of *Iu-di-oh!* is always played by two players. At the beginning of the match, each player chooses exactly one card from his deck. Then, an attribute is randomly chosen. The player whose the chosen attribute is greater in the card he choose wins the match. If the such attribute is equal in both cards, there is a tie.

Marcos and Leonardo are in the big final of the Brazilian *Iu-di-oh!* championship. The great prize is a Dainavision (that is almost as good as a Plaisteition 2!). Given the deck of both players, the card each one chooses and the chosen attribute, determine the winner!

## Input

The input contains several test cases. The first line of each test case contains an integer **N** (1 ≤ **N** ≤ 100), the number of attributes each card contains. The second line contains two integers **M** and **L** (1 ≤ **M**, **L** ≤ 100), the number of cards in Marcos’ and Leonardo’s deck, respectively.

Next **M** lines describe Marcos’ deck. His cards are numbered from 1 to **M**, and *i*-th line describes the *i*-th card. Each line contains **N** integers **ai,1**,**ai,2**,..., **ai,N** (1 ≤ **ai,j** ≤ 109). Integer **ai,j** indicates the *j*-th attribute of the *i*-th card.

Next **L** lines describe Leonardo’s deck. His cards are numbered from 1 to **L** and are described in the same way as Marcos’ deck.

Next line contains two integers **CM** and **CL** (1 ≤ **CM** ≤ **M**, 1 ≤ **CL** ≤ **L**), the cards chosen by Marcos and Leonardo, respectively. Finally, the last line contains an integer **A** (1 ≤ **A** ≤ **N**) indicating the chosen attribute.

The input ends with end-of-file (EOF).

## Output

For each test case, print a line containing “Marcos” if Marcos wins 
the match, “Leonardo” if Leonardo wins the match, or “Empate” in the 
case of a tie (without quotes).

| Input Sample                                                                         | Output Sample |
| ------------------------------------------------------------------------------------ | ------------- |
| 3<br><br>2 2<br><br>3 8 1<br><br>6 7 9<br><br>1 2 3<br><br>8 4 1<br><br>1 2<br><br>2 | Marcos        |

https://www.beecrowd.com.br/judge/en/problems/view/2542

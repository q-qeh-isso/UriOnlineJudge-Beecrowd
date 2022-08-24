# Sudoku

---

The Sudoku puzzle spread quickly across the world, being the most popular hobby in the planet today. Some people, however, fill the matrix incorrectly, breaking the rules. Your task is to write a program that checks whether a filled matrix is a solution to the puzzle or not.

The matrix is a 9 x 9 matrix of integers. To be considered a solution to the puzzle, each row and each column must contain all integer numbers between 1 and 9. Also, if the matrix is partitioned in nine 3 x 3 sub-matrices (as shown below), each one of them must also contain all numbers between 1 and 9. The following matrix is an example of a solution to the puzzle.

<img src="https://resources.beecrowd.com.br/gallery/images/novos/Sudoku.png" title="" alt="" data-align="center">

## Input

Several instances are given. The first line of the input contains **n** > 0, the number of matrices in the input. The following lines describe **n** matrices. Each matrix is described by 9 lines. These lines contain 9 integers each.

## Output

For each instance, your program must print a line containing *"Instancia **k***" , where **k** is the instance number. In the second line, your program must print "*SIM"* (portuguese for *yes*) if the given matrix is a solution to the puzzle, or "*NAO*" (portuguese for *no*) otherwise. Print an empty line after each instance.

| Sample Input                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Sample Output                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| 2<br><br>1 3 2 5 7 9 4 6 8<br><br>4 9 8 2 6 1 3 7 5<br><br>7 5 6 3 8 4 2 1 9<br><br>6 4 3 1 5 8 7 9 2<br><br>5 2 1 7 9 3 8 4 6<br><br>9 8 7 4 2 6 5 3 1<br><br>2 1 4 9 3 5 6 8 7<br><br>3 6 5 8 1 7 9 2 4<br><br>8 7 9 6 4 2 1 5 3<br><br>1 3 2 5 7 9 4 6 8<br><br>4 9 8 2 6 1 3 7 5<br><br>7 5 6 3 8 4 2 1 9<br><br>6 4 3 1 5 8 7 9 2<br><br> 5 2 1 7 9 3 8 4 6<br><br>9 8 7 4 2 6 5 3 1<br><br>2 1 4 9 3 5 6 8 7<br><br>3 6 5 8 1 7 9 2 4<br><br>8 7 9 6 4 2 1 3 5 | Instancia 1<br><br>SIM <br><br><br><br>Instancia 2<br><br>NAO |

https://www.beecrowd.com.br/judge/en/problems/view/1383

# Justifier

---

We have some words and we want to right justify them, that is, align them to the right. Create a program that reads a word and print it all right justified, in the same order as they appear in the input.

## Input

The input contains several test cases. The first line of a test case will contain an integer **N** (1 ≤ **N** ≤ 50) indicating the number of following words. Each word is composed of up to 50 uppercase letters (‘A’-‘Z’) and will contain at least one letter. The end of input is indicated by **N** = 0.

## Output

For each test case print the words padded on the left with space characters so that they are all the same length as thelongest word found in that text. Print an empty line between all the test cases. There must be no trailing spaces printed out, and you should discard any unnecessary leading spaces, so that at least one line on every 
output word starts with a letter.

| Sample Input                                                                                                                                                       | Sample Output                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3<br><br>BOB<br><br>TOMMY<br><br>JIM<br><br>4<br><br>JOHN<br><br>JAKE<br><br>ALAN<br><br>BLUE<br><br>4<br><br>LONGEST<br><br>A<br><br>LONGER<br><br>SHORT<br><br>0 | BOB<br><br>TOMMY<br><br>  JIM<br><br><br><br>JOHN<br><br>JAKE<br><br>ALAN<br><br>BLUE<br><br><br><br> LONGEST<br><br>      A<br><br> LONGER<br><br>  SHORT |

[beecrowd](https://www.beecrowd.com.br/judge/en/problems/view/1273)

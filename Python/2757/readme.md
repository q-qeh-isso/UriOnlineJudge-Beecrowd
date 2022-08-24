# Input and Output of Integers

---

Your teacher would like you to do a program with the following characteristics:

1. Create three variables to store whole numbers;
2. Read the first number, which can be a value in the range of: **-10000 ≤ A ≤ 10000**;
3. Read the second number, which can be a value in the range of: **0 ≤ B ≤ 99**;
4. Read the third number, which can be a value in the range of: **0 ≤ C ≤ 999**;
5. Print the letter A, a space, the equals sign, a blank, the number stored in the first variable, a comma, a blank, the letter B, a blank, the equal sign, a blank, the number stored in the second variable, a comma, a blank, the letter C, a blank, the equal sign, a blank, the number stored in the third variable. *Do not forget to skip line*;Repeat procedure 5, putting the number in a 10-digit spacing and justified to the right;
6. Repeat procedure 5, putting the number in a 10-digit spacing and filled with zeros;
7. Repeat procedure 5 by placing the number in a 10-digit spacing and justified to the left.

## Input

The entry consists of several test files. Each test file has three rows. In the first line has an integer **A** **(-10000 ≤ A ≤ 10000)**. In the second line has an integer **B** **(0 ≤ B ≤ 99)**. In the third line has an integer **C** **(0 ≤ C ≤ 999)**. As shown in the following input samples.

## Output

For each file in the entry, you have an output file. The output file has four rows as described in item 5. As shown in the following output samples.

| Input Samples         | Output Samples                                                                                                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1234<br/> 12 <br/>123 | A = 1234, B = 12, C = 123 <br/>A =       1234, B =         12, C =        123 <br/>A = 0000001234, B = 0000000012, C = 0000000123 <br/>A = 1234      , B = 12        , C = 123 |

| 4567<br/> 78<br/> 789 | A = 4567, B = 78, C = 789 <br/>A =       4567, B =         78, C =        789 <br/>A = 0000004567, B = 0000000078, C = 0000000789 <br/>A = 4567      , B = 78        , C = 789 |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

| -9991<br/> 01 <br/>001 | A = -9991, B = 1, C = 1 <br/>A =      -9991, B =          1, C =          1 <br/>A = -000009991, B = 0000000001, C = 0000000001 <br/>A = -9991     , B = 1         , C = 1 |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

[beecrowd](https://www.beecrowd.com.br/judge/en/problems/view/2757)

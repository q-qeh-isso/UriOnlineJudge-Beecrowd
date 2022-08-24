# The Force Awakens

---

A long time ago, in a galaxy far, far away...

After the decline of the Empire, scavengers are spread around the universe looking for a lost lightsaber. Everyone knows that a lightsaber emits an unique wave pattern: 42 surrounded by 7 all around. You have a wave sensor that scans a terrain with N x M cells. Look at the example below for an 4 x 7 terrain with a lightsaber in it (at position (2,4)).

<img src="https://resources.beecrowd.com.br/gallery/images/contests/935.png" title="" alt="" data-align="center">

You must write a program that, given an N x M terrain, looks for the lightsaber pattern in it. No scan have more than one lightsaber pattern.

## Input

The first line of the input has two positive integers **N** and **M**, representing respectively the number of rows and the number of columns scanned in a terrain (3 ≤ **N**, **M** ≤ 1000). Each of the next **N** lines have **M** integers, describing the values scanned in each cell of the terrain (-100 ≤ **Tij** ≤ 100, for 1 ≤ **i** ≤ **N** and 1 ≤ **j** ≤ **M**).

## Output

The output is a single line with 2 integers **X** and **Y** separated by one space. They represent the (**X**,**Y**)-coordinate of the lightsaber, if it is found. If the terrain doesn't have a lightsaber pattern, **X** and **Y** are both zero.

| Input Samples                                                                                       | Output Samples |
| --------------------------------------------------------------------------------------------------- | -------------- |
| 4 7<br><br>11 12 7 7 7 13 14<br><br>15 6 7 42 7 7 42<br><br>98 -5 7 7 7 42 7<br><br>-1 42 3 9 7 7 7 | 2 4            |

| 4 7  <br>11 12 7 7 7 13 14  <br>15 6 7 12 7 7 42  <br>98 -5 7 7 7 42 7  <br>-1 42 3 9 7 7 7 | 0 0 |
| ------------------------------------------------------------------------------------------- | --- |

| 3 3  <br>7 7 7  <br>7 42 7  <br>7 7 7 | 2 2 |
| ------------------------------------- | --- |

[beecrowd](https://www.beecrowd.com.br/judge/en/problems/view/2163)

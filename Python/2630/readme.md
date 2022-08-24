# Greyscale

---

Some image processing algorithms require preprocessing in which it is necessary to turn a color image into a greyscale image. This conversion can be done in several ways, depending on the result you want to achieve.

To preserve the perception of basic colors by the human eye, an appropriate conversion would be to take 30% of the red component (R), 59% of the green component (G) and 11% of the blue component (B). In mathematical terms:

**P** = 0, 30R + 0, 59G + 0, 11B

Other possible approaches would be to determine the value of **P** through the arithmetic mean of the three components or assign **P** to the highest or the lowest values among the three components.

Given the RGB components of one pixel of the color image, determine the value of pixel **P** of the corresponding gray scale image, determining the conversion to be
 used. Neglect the decimal part of the result, if it exists.

## Input

The input in **T** (1 ≤ **T** ≤ 100) test cases, where the value of **T** is given in the first line of the input. Each test case consists of two lines: the first line contains the conversion to be used: eye for the first approach described, mean for the arithmetic mean, max for the largest component value and min for the lowest component value. The second line contains the **R**, **G**, **B** (0 ≤ **R**, **G**, **B** ≤ 255) values of the colored image pixel.

## Output

For each test case the following message *"Caso #t: P"* should be printed, where **P** is the gray level of the pixel of the grayscale image after the conversion of the colored image pixel. This message must be followed by a line break.

| Input Sample                                                              | Output Sample                                 |
| ------------------------------------------------------------------------- | --------------------------------------------- |
| 3<br/> min<br/> 35 70 35<br/> mean<br/> 10 74 181<br/> eye<br/> 23 78 197 | Caso #1: 35<br/> Caso #2: 88<br/> Caso #3: 74 |

[beecrowd](https://www.beecrowd.com.br/judge/en/problems/view/2630)

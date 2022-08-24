# Which Triangle

---

Given three values, find out if they form a triangle. If so, check if the triangle is scalene, isoceles or equilateral and if it is a triangle rectangle or not.

## Input

Input is given by three integers **A**,**B** e **C** (0 < **A**,**B**,**C** < 105).

## Output

The output must be the one single line containing the string **"Invalido"** if the input values do not represent a triangle.

If the values can be the sides of a triangle the output must be **"Valido-Equilatero"** if such triangle is equilateral, **"Valido-Escaleno"** if it is scalene or **"Valido-Isoceles"** if it is isoceles. The next line of output must read **"Retangulo: S"** if the triangle is rectangle or **"Retangulo: N"** otherwise, as shown in the examples.

| Input Samples | Output Samples |
| ------------- | -------------- |
| 4 6 2         | Invalido       |

| 4 3 3 | Valido-Isoceles  <br>Retangulo: N |
| ----- | --------------------------------- |

| 3 4 5 | Valido-Escaleno  <br>Retangulo: S |
| ----- | --------------------------------- |

[beecrowd](https://www.beecrowd.com.br/judge/en/problems/view/2313)

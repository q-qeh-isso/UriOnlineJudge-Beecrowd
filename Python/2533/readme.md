# Intership

---

*Googlbook* is a famous IT company that opened an office in your town this year! Also, *Googlbook* has just offered interviews to an internship position in the company!

To be interviewed, you need to send some personal information to the company, that will be used to decide who will earn the position. You sent all information they need except one: your API (Academic Performance Index). To get things worse, *Student’s Portal*, the system that provide your API, is not working!

Fortunately, you remember all the grades you got in all **M** subjects you coursed, as well their workloads. You also remember how the API is calculated:

<img src="https://resources.beecrowd.com.br/gallery/images/novos/estagio_fig.png" title="" alt="" data-align="center">

, where **N1**, **N2**, ..., **NM** are your grades in each subject, and **C1**, **C2**, ..., **CM** are the workload of the respective subjects.

Given the grades you got and the workload of each subject, determine your API, so you can send it to Googlbook as soon as possible!

## Input

The input contains several test cases. The first line of each test case contains integer **M** (1 ≤ **M** ≤ 40), the number of subjects you coursed. Each of the next **M** lines describe a subject. Each line contains two integers **Ni** and **Ci** (0 ≤ **Ni** ≤ 100, 30 ≤ **Ci** ≤ 120), indicating the grade you got in that subject and its workload, respectively.

The input ends with end-of-file (EOF).

## Output

For each test case, print a line containing your API. Round and print it with exactly 4 decimal places.

| Input Sample                              | Output Sample |
| ----------------------------------------- | ------------- |
| 3<br><br>70 60<br><br>90 60<br><br>80 120 | 0.8000        |

[beecrowd](https://www.beecrowd.com.br/judge/en/problems/view/2533)

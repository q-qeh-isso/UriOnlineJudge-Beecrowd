# Engine Failure

---

Engineer Joe realizes that always happened a speed fall when the measures of an engine speed slope were made at 10 ms time interval. But this fall happened at varying points at each new engine test.

Joe got curious with that lack of pattern and wants to know, for each engine test, what is the first point in which this speed fall happens.

## Input

The input is an engine test and is given in two lines. The first one has the number **N** of speed measures (1 < **N** ≤ 100). The second line has **N** integers: the engine RPM (revolutions per minute) **Ri** of each measure (0 ≤ **Ri** ≤ 10000, for all **Ri**, such that 1 ≤ **i** ≤ **N**). A measure is considered a speed fall if it is lower than the previous measure.

## Output

The output is the measure index where the first speed fall happened in the test. If no speed fall happens the output must be the number zero.

| Input Samples  | Output Samples |
| -------------- | -------------- |
| 3<br><br>1 4 2 | 3              |

| 5  <br>100 199 199 198 0 | 4   |
| ------------------------ | --- |

| 4  <br>1 2 2 2 | 0   |
| -------------- | --- |

[beecrowd](https://www.beecrowd.com.br/judge/en/problems/view/2167)

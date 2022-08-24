# Pizza Before BH

---

The Nlogonian Aquatic Surf Championship, to be hosted in Bonita Horeleninha (BH) city, is about to start! Before going to BH, you and your **N**-1 friends decided to go for a pizza, so you can relax and have some fun (and, of course, eat!).

At this moment you are choosing the date for the event. To make sure everyone can enjoy it, it was decided that the meeting is to be set in a day so that all the **N** people can show up at the pizzeria on that date.

Given the list of dates considered for the event and the information about which people can show up at which dates, determine if the event can happen and, if it can, its date. If more than one date is possible, the event must occur as early as possible.

## Input

The input contains several test cases. The first line of each test case contains integers **N** and **D** (1 ≤ **N**, **D** ≤ 50), the number of people and the number of considered dates. People are numbered from 1 to **N**. Next **D** lines describe the considered dates. Each line begins with a date in the format *day∕month∕year*. The line is followed by **N** integers **p1**,**p2**,...,**pN**. The integer **pi** is 1 if the *i*-th person can show up at the considered date, or 0 otherwise. It is guaranteed that dates are always valid, and there aren’t leading zeros. 
Also, all dates are given in order, from the earliest to the latest day.

The input ends with end-of-file (EOF).

## Output

For each test case, print one line with the date in the format *day∕month∕year*, *exactly* as it appears in the input. If it is not possible to hold the event, print “*Pizza antes de FdI*” (without quotes).

| Input Sample                                                                                                                                                                                        | Output Sample                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| 4 4<br><br>1/6/2016 0 0 1 0<br><br>12/7/2016 1 1 1 0<br><br>5/10/2016 1 1 1 1<br><br>25/12/2016 0 0 0 0<br><br>5 3<br><br>20/9/2016 0 1 1 1 1<br><br>30/9/2016 1 0 1 1 1<br><br>1/10/2016 1 1 0 1 1 | 5/10/2016<br><br>Pizza antes de FdI |

# Sensor Accuracy

---

The teacher is teaching you about sensors. This is a very important element in many applications. To better understand the concepts of precision, the teacher asked to perform a practical assembly of the Thermo Ind v4.0 sensor in the new Automation laboratory.

As a good student you wrote down the formula for calculating the accuracy of a sensor:

**σ=√∑QT1(Xi−¯¯¯¯¯X)2QT−1**

Where **QT** is the number of times the test was performed, X the value measured in each test and **¯¯¯¯¯X** the mean of the values.

To perform the test you have been doing **H** hours testing, and every **M** minutes you have checked the **X** value of the temperature delivered by the sensor.

Now that you have the measurements, and as you have the ability to program, make a program that delivers sensor accuracy.

## Input

There are several test cases, each case consisting of two lines. The first one contains two values **H** and **M**. The second consists of the floating point values **Xi** indicating the value of each sensor measurement.

It is guaranteed that there will be at least 5 and at most 105 measures per case and that these values are in the interval [0, 255] with two decimal places.

## Output

For each test case, print a single line with a number indicating the sensor's accuracy. The calculated value must be displayed with 5 digits after the decimal point.

| Input Sample                                                                              | Output Sample        |
| ----------------------------------------------------------------------------------------- | -------------------- |
| 1 10 <br/>2.99 2.94 3.02 2.91 3.05 3.11 <br/>2 16 <br/>5.00 5.00 5.00 5.00 5.00 5.00 5.00 | 0.07312 <br/>0.00000 |

[beecrowd](https://www.beecrowd.com.br/judge/en/problems/view/2774)

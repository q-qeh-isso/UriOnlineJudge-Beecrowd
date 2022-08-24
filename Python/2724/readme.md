# Help Patatatitu

---

Juvenal behaved exemplary this year, since he likes chemistry deeply and really want to earn an Alchemy kit. However, Juvenal asked to include some dangerous elements in his kit. As Santa could not deny the request ( how to say no to the world most well behaved children?) asked to poor elf Patatatitu to ensure that the present was safe.

Patatatitu knows a lot about chemistry, and knows every dangerous compound that can be made with the elements available on Juvenal’s kit. Thus, he decided to send a cd together with the gift, containing a program which asserts the safety of Juvenal’s experiments. Everyone agrees that the world’s most well behaved children would never do an experiment without first checking it’s safety as per Santa instructions. However Patatatitu knows nothing about programming and is after someone to help him. Can you help?

To elucidate, Patatatitu explains that a dangerous compound are formed from a mix of elements in theirs chemical formula respecting it’s order and proportions. In this kit it’s possible to add one element each time, in various quantities. Thus, to form chlorine trifluoride (ClF3), an extremely dangerous compound, you must add an atom of 
chlorine (Cl) and three of fluorine (F3), regardless of what was added before or after. ClF4 is not a dangerous compound since it’s a different proportion from ClF3. Similarly, if Mg2F is a dangerous compound, Mg2Fe is safe, since fluorine (F) is different from iron (Fe).

## Input

The input consist of an integer **N** (0 < **N** < 10) which indicates the number of test cases. Each test case have an integer **T** (0 < **T** < 51) which indicates the number of dangerous compounds possible, if th elements are included in the order and proportions shown. Follow **T** lines, each containing a string up to 50 characters representing a formula that generates a dangerous compound if the elements are added in that particular order and proportion. After, is given an integer **U** (0 < **T** < 51) that indicates the number of experiments Juvenal will do. Follow **U** lines each containing an string up to 50 characters representing the elements that Juvenal will use in the order and proportions as they are added.

## Output

The output consist of **U** per test case, which must inform if Juvenal must abort it’s experiment or proceed with the U-th experiment of the test case. If Juvenal must abort print “Abortar”, else if it’s safe print “Prossiga”.Test cases must be separated by a blank 
line .

| Input Sample                                                                                                                                                                                                                                                                                                                                                                                         | Output Sample                                                                                                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3<br/> 3<br/> KH2O<br/> C3H5N3O9<br/> ClF3<br/> 5<br/> WOsFNeSeBrSnAsNOH4C12CuKZrBr<br/> C8H10N4O2C2H7NO3SC6H5NO2<br/> C3H5N3O9ClF3KH20<br/> C3H5N3O9<br/> 4P12Si7CNF12BLiClF312ON12H<br/> 2<br/> H20NaCl<br/> C6H12F2<br/> 4 <br/>H20Na <br/>C6H12F <br/>H20NaCl <br/>C6H12F2 <br/>3 <br/>KBrAsC <br/>Mg2F <br/>CsH <br/>6 <br/>KBrAsCl <br/>Mg2Fe <br/>CsHe <br/>Mg2F <br/>Cl2NaOPMg2F <br/>KBrAsC | Prossiga <br/>Prossiga <br/>Abortar <br/>Abortar <br/>Prossiga <br><br/> Prossiga <br/>Prossiga <br/>Abortar <br/>Abortar <br><br/> Prossiga <br/>Prossiga <br/>Prossiga <br/>Abortar <br/>Abortar <br/>Abortar |

[beecrowd](https://www.beecrowd.com.br/judge/en/problems/view/2724)

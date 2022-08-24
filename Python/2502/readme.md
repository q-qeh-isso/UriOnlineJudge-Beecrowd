# Deciphering the Encrypted Card

---

The oldest known cipher is the Cipher of Caesar. Caesar wrote his letters by exchanging each letter for the next in the alphabet, to avoid that, when the letter was intercepted, enemy could read it. Over time, encryption has acquired better quality, but encryption based on substitution is still an interesting child's play, for example:

ZEN I T  
POLAR

In this child's play, when writing a letter, the letter Z is replaced by the letter P and vice versa, as well as: E by O and so on. The phrase coded as follows: "**Osro roxre osri caftide**" can be deciphered as: "**Este texto esta cifrado**". As the game got serious, you were prompted for a program that decrypts encrypted messages from a supplied key.

## Input

The input contains several test cases. Each test case begins with a line indicating two integers **C** and **N**, 0 < **C** < 21 and 0 < **N** < 100. **C** is the size of the cipher. On the next two lines is the **C**-sized cipher indicating which characters from the first line will be replaced by characters from the second line, a character appears only once, on the first or second line.

The cipher can contain letters from 'A' to 'Z', numbers from '0' to '9' plus white space and some punctuation symbols: '.' ',' ';' ':' '(' ')' '!' and '?'. In the next **N** lines are sentences and sentences encrypted by the cipher provided, which you must decipher. Each line contains a minimum of 1 and a maximum of 1000 characters. Any printable ASCII (non-extended) characters are allowed, in this case no accented characters are present, not even 'ç'.

## Output

For each input test case your program must generate for each sentence line at the input a sentence line with the deciphered output, respecting the capitalization of the letter (capital letters are deciphered as case-sensitive when it is possible to apply, If it is not possible then it will be deciphered as lowercase letters). After each test case, a blank line should be printed, including after the last one.

| Input Sample                                                                                                                                                                                                                                                             | Output Sample                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 5 3<br><br>ZENIT<br><br>POLAR<br><br>Osro roxre osri caftide<br><br>Osri o umi roclaci do ctazregtifai zet subsraruacie<br><br>Zedo sot ficanmolro quobtide i zitrat do umi bei imesrti do roxre<br><br>3 2<br><br>UMA<br><br>123<br><br>C3d3 12 por si<br><br>123 3 123 | Este texto esta cifrado<br><br>Esta e uma tecnica de criptografia por substituicao<br><br>Pode ser facilmente quebrado a partir de uma boa amostra de texto<br><br><br><br>Cada um por si<br><br>uma a uma<br/> |

[beecrowd](https://www.beecrowd.com.br/judge/en/problems/view/2502)

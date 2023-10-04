Detective, one of our team members tracked our target, Vincent the thief. to a hidden warehouse. We belive this is where he's storing the stolen goods.
The entrance to this warehouse is guarded by a digital combination lock. However, our informant isn't entirely certain  about the PIN they witnessed Vicent input.
the keypad has the following layout:
    1, 2 3,
    4, 5, 6,
    7, 8, 9,
    0
    
he noted the pin 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally)
he also mentioned he knows this kind of lock you can enter an unlimited amnout of wrong PINS, but they never finally lock the system or sound the alarm. Thats why we can try it out
all possible variations

all possible in the sense of the observed PIN itself and all varations considerint the adjacent digits
can you help us to find all those variations ? the array should contain all possible pins in ordered in ascending value

input: PIN in string format
output: array of strings (the observed pin itself should be included in the array)

Explanation
If the observed pin is "8", all possible combinations considering horizontal and vertical movements give, us the next output array:
["0","5","7","8","9"]

another example could be for the observed pin "11":
in this case, the output will be:
["11", "12", "14", "21, "22", "22, "24", "41, "42, "44""]

remeber the output should be ordered ascendingly.
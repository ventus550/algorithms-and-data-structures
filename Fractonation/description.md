# Fractonation

### Problem
Given a number $\frac{a}{b}$ find a sequence of numbers $\{a_1, a_2, ... , a_k\}$ such that $\sum \frac{1}{a_i} = \frac{a}{b}$.

### Algorithm
$$
\frac{a_{i+1}}{b_{i+1}} =
\frac{a_i\lceil b_i/a_i \rceil - b_i}{b_i\lceil b_i/a_i \rceil}
$$


### Proof of finiteness
$$
\frac{a_{i+1}}{b_{i+1}} =
\frac{a_i\lceil b_i/a_i \rceil - b_i}{b_i\lceil b_i/a_i \rceil} =
\frac{a_i}{b_i} - \frac{1}{\lceil b_i/a_i \rceil}
$$

Properties:
1. $\lfloor -x \rfloor = -\lceil x \rceil$
2. $n$ $mod$ $d$ $= n - \lfloor n/d \rfloor d$

From them we derive:

$$
\frac{a_{i+1}}{b_{i+1}} =
\frac{a_i\lceil b_i/a_i \rceil - b_i}{b_i\lceil b_i/a_i \rceil} =_1
\frac{-a_i\lceil -b_i/a_i \rceil - b_i}{b_i\lceil b_i/a_i \rceil} =_2
\frac{(-b_i)\bmod a_i}{b_i \lceil b_i/a_i \rceil}
$$



Notice that $a_{i+1} = (-b_i)\bmod a_i < a_i$, so the numerator decreases in each step of the algorithm. Since both the numerator and denominator are nonnegative integers algorithm does indeed end eventually. 

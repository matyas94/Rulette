import random
import os
import time


egyenleg = 20
print(egyenleg)
bet = int(input("Mennyit szeretnél rakni? "))

while bet > egyenleg:
    print("Nem tudsz ennyit rakni.")
    bet = int(input("Mennyit szeretnél rakni? "))

egyenleg -= bet


if 1 == 1:
    r0 = "0"
    r1 = "1"
    r2 = "2"
    r3 = "3"
    r4 = "4"
    r5 = "5"
    r6 = "6"
    r7 = "7"
    r8 = "8"
    r9 = "9"
    r10 = "10"
    r11 = "11"
    r12 = "12"
    r13 = "13"
    r14 = "14"
    r15 = "15"
    r16 = "16"
    r17 = "17"
    r18 = "18"
    r19 = "19"
    r20 = "20"
    r21 = "21"
    r22 = "22"
    r23 = "23"
    r24 = "24"
    r25 = "25"
    r26 = "26"
    r27 = "27"
    r28 = "28"
    r29 = "29"
    r30 = "30"
    r31 = "31"
    r32 = "32"
    r33 = "33"
    r34 = "34"
    r35 = "35"
    r36 = "36"
    r37 = "[1-18]"
    r38 = "[19-36]"
    r39 = "[EVEN]"
    r40 = "[ODD]"
    r41 = "[RED]"
    r42 = "[BLACK]"
    r43 = "[1ST 12]"
    r44 = "[2ND 12]"
    r45 = "[3RD 12]"
    r46 = "[1ST COL]"
    r47 = "[2ND COL]"
    r48 = "[3RD COL]"



    rr0 = [0]
    rr1 = [1]
    rr2 = [2]
    rr3 = [3]
    rr4 = [4]
    rr5 = [5]
    rr6 = [6]
    rr7 = [7]
    rr8 = [8]
    rr9 = [9]
    rr10 = [10]
    rr11 = [11]
    rr12 = [12]
    rr13 = [13]
    rr14 = [14]
    rr15 = [15]
    rr16 = [16]
    rr17 = [17]
    rr18 = [18]
    rr19 = [19]
    rr20 = [20]
    rr21 = [21]
    rr22 = [22]
    rr23 = [23]
    rr24 = [24]
    rr25 = [25]
    rr26 = [26]
    rr27 = [27]
    rr28 = [28]
    rr29 = [29]
    rr30 = [30]
    rr31 = [31]
    rr32 = [32]
    rr33 = [33]
    rr34 = [34]
    rr35 = [35]
    rr36 = [36]
    rr37 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    rr38 = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    rr39 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
    rr40 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
    rr41 = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    rr42 = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    rr43 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    rr44 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    rr45 = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    rr46 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    rr47 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    rr48 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
print(f"""
|--------------|
|       {r0}      |
|--------------|
|  {r1} |  {r2} |  {r3} |
|--------------|
|  {r4} |  {r5} |  {r6} |
|--------------|
|  {r7} |  {r8} |  {r9} |
|--------------|
| {r10} | {r11} | {r12} |
|--------------|
| {r13} | {r14} | {r15} |
|--------------|
| {r16} | {r17} | {r18} |
|--------------|
| {r19} | {r20} | {r21} |
|--------------|
| {r22} | {r23} | {r24} |
|--------------|
| {r25} | {r26} | {r27} |
|--------------|
| {r28} | {r29} | {r30} |
|--------------|
| {r31} | {r32} | {r33} |
|--------------|
| {r34} | {r35} | {r36} |
|--------------|

{r37}
{r38}
{r39}
{r40}
{r41}
{r42}
{r43}
{r44}
{r45}
{r46}
{r47}
{r48}
Ha kell segítség akkor :'help', ha nem nyomj entert.""")

help = input("")
if help == "help":
    print("""
[1-18]: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
[19-36]: 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36
[EVEN]: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35
[ODD]: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36
[RED]: 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
[BLACK]: 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35
[1ST 12]: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
[2ND 12]: 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24
[3RD 12]: 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36
[1ST COL]: 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34
[2ND COL]: 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35
[3RD COL]: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36""")

win = 29
szam = input("Hova szeretnél tenni?")
if 1 == 1:
    if szam == 0:
        r0 = "X"
        win = 0
    elif szam == 1:
        r1 = "X"
        win = 1
    elif szam == 2:
        r2 = "X"
        win = 2
    elif szam == 3:
        r3 = "X"
        win = 3
    elif szam == 4:
        r4 = "X"
        win = 4
    elif szam == 5:
        r5 = "X"
        win = 5
    elif szam == 6:
        r6 = "X"
        win = 6
    elif szam == 7:
        r7 = "X"
        win = 7
    elif szam == 8:
        r8 = "X"
        win = 8
    elif szam == 9:
        r9 = "X"
        win = 9
    elif szam == 10:
        r10 = "X"
        win = 10
    elif szam == 11:
        r11 = "X"
        win = 11
    elif szam == 12:
        r12 = "X"
        win = 12
    elif szam == 13:
        r13 = "X"
        win = 13
    elif szam == 14:
        r14 = "X"
        win = 14
    elif szam == 15:
        r15 = "X"
        win = 15
    elif szam == 16:
        r16 = "X"
        win = 16
    elif szam == 17:
        r17 = "X"
        win = 17
    elif szam == 18:
        r18 = "X"
        win = 18
    elif szam == 19:
        r19 = "X"
        win = 19
    elif szam == 20:
        r20 = "X"
        win = 20
    elif szam == 21:
        r21 = "X"
        win = 21
    elif szam == 22:
        r22 = "X"
        win = 22
    elif szam == 23:
        r23 = "X"
        win = 23
    elif szam == 24:
        r24 = "X"
        win = 24
    elif szam == 25:
        r25 = "X"
        win = 25
    elif szam == 26:
        r26 = "X"
        win = 26
    elif szam == 27:
        r27 = "X"
        win = 27
    elif szam == 28:
        r28 = "X"
        win = 28
    elif szam == 29:
        r29 = "X"
        win = 29
    elif szam == 30:
        r30 = "X"
        win = 30
    elif szam == 31:
        r31 = "X"
        win = 31
    elif szam == 32:
        r32 = "X"
        win = 32
    elif szam == 33:
        r33 = "X"
        win = 33
    elif szam == 34:
        r34 = "X"
        win = 34
    elif szam == 35:
        r35 = "X"
        win = 35
    elif szam == 36:
        r36 = "X"
        win = 36
    elif szam == "[1-18]":
        r37 = "X"
        win = 37
    elif szam == "[19-36]":
        r38 = "X"
        win = 38
    elif szam == "[EVEN]":
        r39 = "X"
        win = 39
    elif szam == "[ODD]":
        r40 = "X"
        win = 40
    elif szam == "[RED]":
        r41 = "X"
        win = 41
    elif szam == "[BLACK]":
        r42 = "X"
        win = 42
    elif szam == "[1ST 12]":
        r43 = "X"
        win = 43
    elif szam == "[2ND 12]":
        r44 = "X"
        win = 44
    elif szam == "[3RD 12]":
        r45 = "X"
        win = 45
    elif szam == "[1ST COL]":
        r46 = "X"
        win = 46
    elif szam == "[2ND COL]":
        r47 = "X"
        win = 47
    elif szam == "[3RD COL]":
        r48 = "X"
        win = 48


nyero = random.randint(0,36)
print(nyero)
if nyero == szam:
    egyenleg += (bet*36)
elif (szam == "[1-18]" or szam == "[19-36]" or szam == "[EVEN]" or szam == "[ODD]" or szam == "[RED]" or szam == "[BLACK]") and (nyero in rr37 or nyero in rr38 or nyero in rr39 or nyero in rr40 or nyero in rr41 or nyero in rr42):
    egyenleg += (bet*2)
elif (szam == "[1ST 12]" or szam == "[2ND 12]" or szam == "[3RD 12]" or szam == "[1ST COL]" or szam == "[2ND COL]" or szam == "[3RD COL]") and (nyero in rr43 or nyero in rr44 or nyero in rr45 or nyero in rr46 or nyero in rr47 or nyero in rr48):
    egyenleg += (bet*3)
print(egyenleg)
print(win)

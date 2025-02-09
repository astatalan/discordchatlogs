import pyperclip
import random
def maindef(funcarray, streak, outt, lastfunc_index, iin, spacestreak, lastspace):
    arithmetic_sequence_list = [0 + i * 1 for i in range((len(funcarray) - 0 + 1 - 1) // 1)]
    if (iin == '\r'):
        return None, streak, outt, lastfunc_index, None, spacestreak, lastspace
    if (iin == ' ') or (iin == '\n'):
        if lastspace == '↗️':
            exitprob = [1, 1 + spacestreak]
        else:
            exitprob = [1 + spacestreak, 1]
        newspace = random.choices(['↗️' + iin,'↘️' + iin], weights = exitprob)[0]
        if newspace[0] == lastspace:
            spacestreak += 1
        else:
            lastspace = newspace[0]
            spacestreak = 1
        outt.extend(newspace)
        return None, streak, outt, lastfunc_index, None, spacestreak, lastspace
    exitprob = [1 + streak / (len(funcarray) - 1)] * len(funcarray)
    exitprob[lastfunc_index] = 1
    newfunc=random.choices(arithmetic_sequence_list, weights = exitprob)[0]
    if lastfunc_index == newfunc:
        streak += 1
    else:
        lastfunc_index = newfunc
        streak = 1
    outt.extend(funcarray[newfunc](iin))
    return None, streak, outt, lastfunc_index, None, spacestreak, lastspace
numbertable='⁰0₀¹1₁²2₂³3₃⁴4₄⁵5₅⁶6₆⁷7₇⁸8₈⁹9₉'
inputt=[]
for b in pyperclip.paste():
	inputt.append(b)
if (b != ' ') and (b != '\n'):
	inputt.append('\n'*('\n' in inputt)+' '*(1-('\n' in inputt)))
funcarray=[]
###############################################################################
#insert functions into funcarray
def ___capitalize(strng):
    if strng in numbertable:
        return [numbertable[numbertable.index(strng)//3*3]]
    return [strng.upper()]
funcarray.append(___capitalize)

def ___lowercize(strng):
    if strng in numbertable:
        return [numbertable[numbertable.index(strng)//3*3+2]]
    return [strng.lower()]
funcarray.append(___lowercize)









###############################################################################
if len(funcarray)<2:
    exit()
streak = 0
outt = []
nullvar = None
nullvar0 = None
lastfunc_index = 0
iin_index = 0
iin = inputt[iin_index]
spacestreak = 0
lastspace = '➡️'



while True:
    nullvar, streak, outt, lastfunc_index, nullvar0, spacestreak, lastspace = maindef(funcarray, streak, outt, lastfunc_index, iin, spacestreak, lastspace)
    iin_index += 1
    if iin_index >= len(inputt):
        break
    iin=inputt[iin_index]
pyperclip.copy("".join(outt))
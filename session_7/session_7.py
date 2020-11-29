# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 18:47:54 2020

@author: Mutum
"""

# 1
# Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not. 
# You can use a pre-calculated list/dict to store fab numbers till 10000

def generate_fibo(n):
    '''
    Function to generate Fibonacci series upto n`th term
    
    Input = an integer say 5
    Output = fibonacci series upto 5th term --> [0, 1, 1, 2, 3]
    '''
    # The Fibonacci numbers are the numbers in the following integer sequence.
    #       0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
    
    first = 0  # first term
    second = 1  # second term
    result = []
    for num in range(n):
        if type(n) != int:
            raise TypeError("Input only integer value")
        if num <2:
            result.append(num)
        else:
            result.append(result[len(result)-2] + result[len(result)-1])
    return result

fibo = generate_fibo(100000)  # fibonacci series upto 100,000 th term

def check_fibo_num(a):
    
    ''' Check any number it is present in fibonacci series upto 100,000 th term'''
    
    return bool(list(filter(lambda x : x in fibo,[a for num in range(1)])))

check_fibo_num(0)

# 2

# Using list comprehension (and zip/lambda/etc if required) write an expression that:
# - add 2 iterables a and b such that a is even and b is odd
# - strips every vowel from a string provided (tsai>>t s)
# - acts like a ReLU function for a 1D array
# - acts like a sigmoid function for a 1D array
# - takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn



#  add 2 iterables a and b such that a is even and b is odd

import random
import math

a = [random.randint(0,150) for num in range(0,21)]  # making a list of integers
b = [random.randint(0,150) for num in range(0,21)]  # making a list of integers

sum([x for x in list(filter(lambda x : x %2 == 0,a)) + list(filter(lambda x : x %2 != 0,b))  ])

#[x+y for x,y in zip(filter(lambda x : x %2 == 0,a),filter(lambda x : x %2 != 0,b)) ]

# strips every vowel from a string provided (tsai>>t s)

string  = "tsai"

[x for x in string if str.lower(x) not in "aeiou"]

"".join([x for x in string if str.lower(x) not in "aeiou"])

# acts like a ReLU function for a 1D array


a = [random.randint(-50,150) for num in range(0,21)]
print(a)

print([max(0,x) for x in a])

# acts like a sigmoid function for a 1D array

b = [random.randint(-50,150) for num in range(0,21)]
print(b)

print([round(1 / (1+ math.exp(-x)) ,2) for x in b])


# takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn

char_ascii = [x for x in range(97,123) ]  # ascii for a and z are 97 and 122 respectively

#[chr(ord(char)+5) for char in "tsaz"]

string  = "tsai"

"".join([(lambda x : chr(ord(x)+5) if (ord(x)+5 <122)  else chr(96 + 5 - (ord(x) - 122)) ) (x) for x in string])

# 3

# A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of
# the swear words mentioned in https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt 

profanity = ['4r5e', '5h1t', '5hit', 'a55', 'anal', 'anus', 'ar5e', 'arrse', 'arse', 'ass', 'ass-fucker', 'asses', 'assfucker', 'assfukka', 'asshole', 'assholes', 'asswhole', 'a_s_s', 'b!tch', 'b00bs', 'b17ch', 'b1tch', 'ballbag', 'balls', 'ballsack', 'bastard', 'beastial', 'beastiality', 'bellend', 'bestial', 'bestiality', 'bi+ch', 'biatch', 'bitch', 'bitcher', 'bitchers', 'bitches', 'bitchin', 'bitching', 'bloody', 'blow', 'job', 'blowjob', 'blowjobs', 'boiolas', 'bollock', 'bollok', 'boner', 'boob', 'boobs', 'booobs', 'boooobs', 'booooobs', 'booooooobs', 'breasts', 'buceta', 'bugger', 'bum', 'bunny', 'fucker', 'butt', 'butthole', 'buttmunch', 'buttplug', 'c0ck', 'c0cksucker', 'carpet', 'muncher', 'cawk', 'chink', 'cipa', 'cl1t', 'clit', 'clitoris', 'clits', 'cnut', 'cock', 'cock-sucker', 'cockface', 'cockhead', 'cockmunch', 'cockmuncher', 'cocks', 'cocksuck', 'cocksucked','cocksucker', 'cocksucking', 'cocksucks','cocksuka', 'cocksukka', 'cok', 'cokmuncher', 'coksucka', 'coon', 'cox', 'crap', 'cum', 'cummer', 'cumming', 'cums', 'cumshot', 'cunilingus', 'cunillingus', 'cunnilingus', 'cunt', 'cuntlick','cuntlicker','cuntlicking', 'cunts', 'cyalis', 'cyberfuc', 'cyberfuck', 'cyberfucked', 'cyberfucker', 'cyberfuckers', 'cyberfucking', 'd1ck', 'damn', 'dick', 'dickhead', 'dildo', 'dildos', 'dink', 'dinks', 'dirsa', 'dlck', 'dog-fucker', 'doggin', 'dogging', 'donkeyribber', 'doosh', 'duche', 'dyke', 'ejaculate', 'ejaculated', 'ejaculates', 'ejaculating', 'ejaculatings', 'ejaculation', 'ejakulate', 'fuck', 'fucker', 'f4nny', 'fag', 'fagging', 'faggitt', 'faggot', 'faggs', 'fagot', 'fagots', 'fags', 'fanny', 'fannyflaps', 'fannyfucker', 'fanyy', 'fatass', 'fcuk', 'fcuker', 'fcuking', 'feck', 'fecker', 'felching', 'fellate', 'fellatio', 'fingerfuck','fingerfucked','fingerfucker','fingerfuckers', 'fingerfucking','fingerfucks','fistfuck', 'fistfucked', 'fistfucker','fistfuckers','fistfucking', 'fistfuckings', 'fistfucks', 'flange', 'fook', 'fooker', 'fuck', 'fucka', 'fucked', 'fucker', 'fuckers', 'fuckhead', 'fuckheads', 'fuckin', 'fucking', 'fuckings', 'fuckingshitmotherfucker', 'fuckme', 'fucks', 'fuckwhit', 'fuckwit', 'fudge', 'packer', 'fudgepacker', 'fuk', 'fuker', 'fukker', 'fukkin', 'fuks', 'fukwhit', 'fukwit', 'fux', 'fux0r', 'f_u_c_k', 'gangbang', 'gangbanged', 'gangbangs', 'gaylord', 'gaysex', 'goatse', 'God', 'god-dam', 'god-damned', 'goddamn', 'goddamned', 'hardcoresex', 'hell', 'heshe', 'hoar', 'hoare', 'hoer', 'homo', 'hore', 'horniest', 'horny', 'hotsex', 'jack-off',  'jackoff', 'jap', 'jerk-off', 'jism', 'jiz', 'jizm', 'jizz', 'kawk', 'knob', 'knobead', 'knobed', 'knobend', 'knobhead', 'knobjocky', 'knobjokey', 'kock', 'kondum', 'kondums', 'kum', 'kummer', 'kumming', 'kums', 'kunilingus', 'l3i+ch', 'l3itch', 'labia', 'lmfao', 'lust', 'lusting', 'm0f0', 'm0fo', 'm45terbate', 'ma5terb8', 'ma5terbate', 'masochist', 'master-bate', 'masterb8', 'masterbat*', 'masterbat3', 'masterbate', 'masterbation', 'masterbations', 'masturbate', 'mo-fo', 'mof0', 'mofo', 'mothafuck', 'mothafucka', 'mothafuckas', 'mothafuckaz', 'mothafucked', 'mothafucker', 'mothafuckers', 'mothafuckin', 'mothafucking', 'mothafuckings', 'mothafucks', 'mother', 'fucker', 'motherfuck', 'motherfucked', 'motherfucker', 'motherfuckers', 'motherfuckin', 'motherfucking', 'motherfuckings', 'motherfuckka', 'motherfucks', 'muff', 'mutha', 'muthafecker', 'muthafuckker', 'muther', 'mutherfucker', 'n1gga', 'n1gger', 'nazi', 'nigg3r', 'nigg4h', 'nigga', 'niggah', 'niggas', 'niggaz', 'nigger', 'niggers', 'nob', 'nob', 'jokey', 'nobhead', 'nobjocky', 'nobjokey', 'numbnuts', 'nutsack', 'orgasim', 'orgasims', 'orgasm', 'orgasms', 'p0rn', 'pawn', 'pecker', 'penis', 'penisfucker', 'phonesex', 'phuck', 'phuk', 'phuked', 'phuking', 'phukked', 'phukking', 'phuks', 'phuq', 'pigfucker', 'pimpis', 'piss', 'pissed', 'pisser', 'pissers', 'pisses', 'pissflaps', 'pissin', '', 'pissing', 'pissoff', '', 'poop', 'porn', 'porno', 'pornography', 'pornos', 'prick', 'pricks', '', 'pron', 'pube', 'pusse', 'pussi', 'pussies', 'pussy', 'pussys', '', 'rectum', 'retard', 'rimjaw', 'rimming', 's', 'hit', 's.o.b.', 'sadist', 'schlong', 'screwing', 'scroat', 'scrote', 'scrotum', 'semen', 'sex', 'sh!+', 'sh!t', 'sh1t', 'shag', 'shagger', 'shaggin', 'shagging', 'shemale', 'shi+', 'shit', 'shitdick', 'shite', 'shited', 'shitey', 'shitfuck', 'shitfull', 'shithead', 'shiting', 'shitings', 'shits', 'shitted', 'shitter', 'shitters', 'shitting', 'shittings', 'shitty', 'skank', 'slut', 'sluts', 'smegma', 'smut', 'snatch', 'son-of-a-bitch', 'spac', 'spunk', 's_h_i_t', 't1tt1e5', 't1tties', 'teets', 'teez', 'testical', 'testicle', 'tit', 'titfuck', 'tits', 'titt', 'tittie5', 'tittiefucker', 'titties', 'tittyfuck', 'tittywank', 'titwank', 'tosser', 'turd', 'tw4t', 'twat', 'twathead', 'twatty', 'twunt', 'twunter', 'v14gra', 'v1gra', 'vagina', 'viagra', 'vulva', 'w00se', 'wang', 'wank', 'wanker', 'wanky', 'whoar', 'whore', 'willies', 'willy', 'xrated', 'xxx']

para = "Those strong feelings drive some people to try to stamp profanity out. 5hit After cable news networks played the infamous video of Donald Trump saying he grabs women “by the pussy,” about two dozen people filed indecency complaints with the Federal Communication Commission—which regulates the use of profanity on public airwaves—according to records obtained by Morning Consult. “Some consumers are easily offended,” a lawyer interviewed by Morning Consult said, “while others have a high tolerance for what is being shown on television.”Experts like Jay will tell you that many of the reasons people often oppose profanity are based on “myths,” and academics have worked to debunk them. Bergen dedicates a whole chapter in his book to taking down a (flawed) study that suggested profanity harms children. Jay, meanwhile, recently took on the notion that people only swear because they’re not intelligent enough to express themselves another way. What he found is that people with larger vocabularies can actually generate more swear words than people with smaller ones.Jay has also found that the soap-in-the-mouth doesn’t work. In fact, there’s reason to believe that the more kids are sheltered from these words, the more impressive they become. In a follow up to the ice water study, for instance, the same researchers found that the pain-easing effect of uttering swear words was more acute among people who swore less. Use it all the time and you habituate; the words lose their oomph. "

any([(x in profanity) for x in para.split()])

# list(filter(None,[(x in profanity) for x in para.split()]))


# 4

# Using reduce function: PTS:100
# - add only even numbers in a list
# - find the biggest character in a string (printable ascii characters)
# - adds every 3rd number in a list

from functools import reduce

# add only even numbers in a list

a = [32, 98, 21, 121]

reduce(lambda x,y: x+y ,filter(lambda x: x % 2 == 0,a))

# find the biggest character in a string (printable ascii characters)

string = "biggest"

#ord("z")

reduce(lambda x,y : chr(max(ord(x),ord(y))),string)

# adds every 3rd number in a list

l1 = [1,2,3,4,5,6,7,8,9]

reduce(lambda x,y : x+ y ,filter(lambda x : (l1.index(x) +1 ) %3 ==0 ,l1)) # sums every 3rd element in a list

# 5
# Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999


[ "KA" + str(random.randint(11,100)) + random.choice([chr(x) for x in range(65,91)]) + random.choice([chr(x) for x in range(65,91)]) + str(random.randint(1000+1,9999+1))  for num in range(0,15)]

# # 6
# Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided. Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided

from functools import partial

# Writing the same expression/functions in question 5 where KA can be changed to DL, and 1000/9999 ranges can be provided

def vehicle_number(start = 1000,end = 9999,state = "KA"):
    '''
    Return 15 random vehicle number plate
    
    Inputs:
    state : two letter of state abbrevation, default "KA"
    start : starting number (exclusive) for generation random number for the number plate
    end : ending number (exclusive) for generation random number for the number plate
    
    Outputs: a list of 15 number plate like 'KA24FO5393'
        
    '''
    #print(start,end)
    return [ state + str(random.randint(11,100)) + random.choice([chr(x) for x in range(65,91)]) + random.choice([chr(x) for x in range(65,91)]) + str(random.randint(start+1,end+1))  for num in range(0,15)]


vehicle_number()  # generate 15 number plate

vehicle_number(state = "DL",start= 2000,end= 9999) # generate 15 number plate changing state "DL" and range change for random number generation


# use a partial function such that 1000/9999 are hardcoded, but KA can be provided

p = partial(vehicle_number,1000,9999)  # number range are hardcoded

p(state = "MP")  # allows only to change the state argument, the number range cannot be change here - will throw error


'''
TODO: Post processing
IF there's 2 words joined together, ie, model missed out the space in between the 2 words, this model 
will detect it and split it into 2 words
'''

from math import log
import nltk
from nltk.corpus import brown

def eng_words_list():
    # empty list to read list from a file
    words= []
    
    # open file and read the content in a list
    with open('125k_words.txt', 'r') as fp:
        for line in fp:
            # remove linebreak from a current name
            # linebreak is the last character of each line
            x = line[:-1]
    
            # add current item to the list
            if len(x) != 1:
                words.append(x)
    
    # display list
    return words

def infer_spaces(s):
    # Import words corpus from brown nltk
    words = list(brown.words())
    #words = eng_words_list()
    wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
    maxword = max(len(x) for x in words)

    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))


s = 'thumbgreenappleactiveassignmentweeklymetaphor'
print(infer_spaces(s))

res = [[[[12, 12], [71, 12], [71, 33], [12, 33]], '46IIII'], [[[288, 10], [352, 10], [352, 34], [288, 34]], '21:29'], [[[444, 8], [580, 8], [580, 32], [444, 32]], 'VFNHD 46 36%'], [[[117, 58], [442, 58], [442, 126], [117, 126]], 'Binance English EN G LI 5 H 57.8K members'], [[[29, 156], [523, 156], [523, 284], [29, 284]], "Pinned Message Binance Lists Red Pulse (RPX) https:/Isupp Clc SVU L' (」! 11/! 乙 hehe crypto expert 21.26"], [[[584, 172], [613, 172], [613, 200], [584, 200]], '义'], [[[115, 314], [504, 314], [504, 621], [115, 621]], 'Binance [Official] Hello _ Binance is doing a giveaway to their Telegram members。 To receive your free 0.5 BTC all you need to do is to Withdraw 0.01 BTC to the following address'], [[[118, 651], [507, 651], [507, 719], [118, 719]], '13mcUEN741yBYFhVTkHUhX BbiQ3d1BeVSj'], [[[117, 754], [510, 754], [510, 858], [117, 858]], 'You have to do that So We can get your address to send back your BTC.'], [[[620, 792], [640, 792], [640, 819], [620, 819]], ''], [[[9, 891], [518, 891], [518, 959], [9, 959]], 'Be fast bacause We Will give TINANCE only 1000 of BTC only! 21.26'], [[[117, 992], [462, 992], [462, 1123], [117, 1123]], 'Steven Get free btc etch eos bps:Llbitcysaaslianbiie Jinvite?code=43137 01'], [[[36, 1058], [60, 1058], [60, 1088], [36, 1088]], '5'], [[[91, 1146], [233, 1146], [233, 1189], [91, 1189]], 'Message'], [[[489, 1140], [534, 1140], [534, 1186], [489, 1186]], '@'], [[[546, 922], [645, 922], [645, 973], [546, 973]], '']]
res[3][1].split()
len(res[0][1])

i=res[2][1]
word = 'iamaboy'

for i in res:
    sentence = i.split()
    for word in sentence:
        print (word)
        if len(sentence) > 1:
            len(sentence)
            print(infer_spaces(word)) 
    


    
"""Words per Minute Calculator! (WPM)"""

import time

phrase = "Sedimentary rocks are one of three main types of rocks, along with igneous and metamorphic."


word_count = len(phrase.split())

begin = input('Please type: ' + phrase + '\n' + 'Press enter when ready!')

t1 = time.time()
attempt = input('\n')
t2 = time.time()

time_taken = (t2 - t1) / 60
wpm = str(round(word_count / time_taken, 2))

if attempt == phrase:
    print('\n' + 'Your WPM is: ' + wpm)
else:
    print('\n' + "Typed incorrectly. Please try again!")

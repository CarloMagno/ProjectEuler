'''
Created on 03/12/2012

@author: Carlitos
'''
from time import time

## Check if one phrase has exactly the same letter set as the other.
#def isAnagram(one, two):
#  # First divide each phrase into a list of words, then join the words into
#  # a string.  Then compare the alphabetically-sorted strings for equality.
#  # Apostrophes are stripped from the words.
#  list1 = str(one).split()
#  list2 = str(two).split()
#  word1 = ""; word2 = ""
#  sorted_joined_str1 = ""; sorted_joined_str2 = ""
#  for word in list1:
#      word1 += word
#  sorted_joined_str1 += ''.join(sorted(word1, key=str.lower)).lower().replace("'","")
# 
#  for word in list2:
#      word2 += word
#  sorted_joined_str2 += ''.join(sorted(word2, key=str.lower)).lower().replace("'","")
# 
#  if sorted_joined_str1 == sorted_joined_str2: return True
#  else: return False

def isAnagram(a, b):
    cad1, cad2 = str(a), str(b)
    if len(cad1) == len(cad2):
        cad1 = sorted(cad1)
        cad2 = sorted(cad2)
        for i in range(len(cad1)):
            if not cad1[i] == cad2[i]:
                return False
    else:
        return False
    
    return True

def reto52():
    found = False
    i = 1
    while not found:
        if (isAnagram(i, i*2) and
            isAnagram(i, i*3) and
            isAnagram(i, i*4) and
            isAnagram(i, i*5) and
            isAnagram(i, i*6)):
            found = True
            print i
        i += 1
        
if __name__ == '__main__':
    ini = time()
    reto52()
    print "Tiempo =",time()-ini,"sg"
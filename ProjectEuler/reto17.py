'''
Created on 21/11/2012

@author: Carlitos
'''

dict = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",15:"fifteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",}

def formaCadena(num):
    res = ""
    if dict.has_key(num):
        res = dict.get(num)
    else:
        if num == 1000:
            res = "onethousand"
        elif num >= 100:
            res = dict.get(num//100)
            res += "hundred"
            if num%100 != 0:
                res += "and"
                res += formaCadena(num%100)
        elif num < 90 and num > 79:
            res = "eighty"
            res += dict.get(num%10)    
        elif num < 60 and num > 49:
            res = "fifty"
            res += dict.get(num%10)
        elif num < 50 and num > 39:
            res = "forty"
            res += dict.get(num%10)
        elif num < 40 and num > 29:
            res = "thirty"
            res += dict.get(num%10)
        elif num < 30 and num > 19:
            res = "twenty"
            res += dict.get(num%10)
        elif num > 20:
            res = dict.get(num//10)
            res += "ty"
            res += dict.get(num%10)
        elif num == 18:
            res = "eighteen"
        elif num > 10:
            res = dict.get(num%10)
            res += "teen"
    return res

if __name__ == "__main__":
    map = {}
    sum = 0
    for i in range(1,1000+1):
        str = formaCadena(i)
        sum += len(str)
        print i,str
    print sum
#    prueba = "one hundred and fifteen"
#    reduce(lambda x,y: x+y,prueba.split())
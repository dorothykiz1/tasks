# 1- celcius to Fahrenheit

def convert(Celsius):
    Fahrenheit = (Celsius * 1.8) + 32
    print( f"The Fahrenheit temperature of Celcius temperature {Celsius} is {Fahrenheit} .")

convert(10)



# 2- reverse string changing to a list using slicing
def reverse_string(s):
   list1 = list(s)[::-1]
   #converting a list back to astring
   print(f'the reverse of {s} is {'.join(list1)} .' )

reverse_string('keza')



# 3- factorial
def find_factorial(n):
    factorial=1

    if n<0:
        print ('The number is a negative please enter a positive number!')
    elif n==0:
        print(f'the factorial of {n} \szis 0 ')

    else:
        for num in range(1,n+1):
            factorial=factorial*num

        print(f'the factorial of {n} is {factorial}')

find_factorial(0)




#4 -length of the longest word

# take the string as the functional argument
# split the string and return alist of all words separated by space
# traverse through the list and find out the string with max length,store info in some variable
def length_longest(sentence):
    words = sentence.split()
    max_length= 0
    max_word=""
    for word in words:
        if len(word)> max_length:
            max_length=len(word)
            max_word =word
    print(max_length) 

length_longest('is international')    




#5-
        


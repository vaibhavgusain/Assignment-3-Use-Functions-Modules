# Write a Python function that accepts a string 
# and calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'

# Expected Output :

# No. of Upper case characters : 3

# No. of Lower case Characters : 12

def characters(sample):
    upper_case = 0
    lower_case = 0
    for i in sample:
        if i.isupper():
            upper_case+=1
        elif i.islower():
            lower_case+=1
        else:
            pass
    print("No. of Upper case characters :",upper_case)            
    print("No. of Lower case characters :",lower_case)

characters("The quick Brow Fox")                

       
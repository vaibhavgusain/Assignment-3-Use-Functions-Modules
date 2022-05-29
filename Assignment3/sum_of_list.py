#  Write a Python function to sum all the numbers in a list.

# Sample List : (8, 2, 3, 0, 7)

# Expected Output : 20

# def sample_list(*numbers):
#     Sum_of_list=0
#     for i in numbers:
#         Sum_of_list+=i
#     print("Expected Outcome :",Sum_of_list)
        
# sample_list(8,2,3,0,7)



# creating a list
list1 = [8,2,3,0,7]
 
# creating sum_list function
def sumOfList(list, size):
   if (size == 0):
     return 0
   else:
     return list[size - 1] + sumOfList(list, size - 1)
  
# Driver code    
total = sumOfList(list1, len(list1))
 
print("Sum of all elements in given list: ", total)



        

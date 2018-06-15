# Dependencies
import os
import csv


budget_data = os.path.join("GWDC201805DATA3-Class-Repository-DATA/Homework/03-Python/Instructions/PyBank/raw_data","budget_data_1.csv")

# Open and read csv
with open (budget_data, newline="") as csvfile:
    csv_reader=csv.reader(csvfile,delimiter=",")

    # skipping the next line to avoid the header
    next(csv_reader,None) 


   #create an empty list and fill it with revenue data to make it easier to count the number -
   # of months
   #The 'count' is the number of Total Month.
    cr_list=[]
    count = 0
    for x in csv_reader:
        cr_list.append(x[1])
        count = count + 1
      
    # Create a function that calulates and returns a sum from the newly created list.
    #The total sum is the Total Revenue.


    def sumx(lists):

         """Sums all numbers in a list."""
         sumx = 0
         for x in lists:
              sumx = sumx + int(x)
         return sumx
    # Create a function to find the min. and max. value from the created list and returns-
    # the max and min value.
       

    def min_max(numbers):
        """Finds the min and max value in a list of numbers."""
        return min(numbers), max(numbers)

 #  A tuple of both values are returned
    both = min_max(cr_list)
     
 

# # We can "Unpack" the return into separate variables
    min_number, max_number = min_max(cr_list)
# The max and min value corespond to the greatest and smallest value in the data.


################################################################################    
   #counter=2
    #for y in cr_list : 
        
       #if y == max_number:
            #print(counter)
          
        #else:
            #counter= counter+1

################################################################################
  
    # To find the index number where the min. value is found from the created list
    #iteration =2       
    #for z in cr_list :

     #   if z == min_number:
        #    print(iteration) 
               
      #  else:
       #     iteration=iteration+1    
         
#####################################################################################        
    # To find the average value-
    #    the total sum is divided by the total values counted
        

    avg = int(sumx(cr_list)/count)



    # print all the values in a presentable format with date included:
    print  ("Financial Analysis  ")
    print("---------------------------------------")


    print(" Total Month :  ", count) 
    print(" Total Revenue :   ","$",sumx(cr_list))
    print(" Averag Revenue change :  ", "$",avg)

    #Read the csv reader to find the correponding date to the maximum value tat we find from-
    # the created list to the corespoding  original data.
with open (budget_data, newline="") as csvfile:        
    csv_reader=csv.reader(csvfile,delimiter=",")
    for row in csv_reader: 
        for value in row:
            if value == max_number:
                increased=row
                print(" Greatest Increase in Revenue :  ", increased)
             


    #Read the csv reader to find the corresponding date and value from the original data        
with open (budget_data, newline="") as csvfile:        
    csv_reader=csv.reader(csvfile,delimiter=",")
    for lin in csv_reader: 
        for minimum in lin:
            if minimum == min_number:
                decreased=lin
                print(" Greatest Decrease in Revenue :   ",decreased) 

with open("Analysis_file.txt","w") as f:
    print('Financial Analysis', file=f)
    print('---------------------------', file=f)
    print('Total month:',count, file =f) 
    print('Total Revenue :   ','$',sumx(cr_list), file=f)
    print('Greatest Increase in Revenue :  ',increased, file=f)
    print('Greatest Decrease in Revenue :   ',decreased, file=f) 
f.close()               
 

    
    
    
    
    





        
       
    
    
   







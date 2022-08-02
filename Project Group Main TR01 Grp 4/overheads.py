#Creating an empty list for storing the overhead float values
overhead_list = []
category_list = []

#Creating a dictionary for storing data from csv file without headers category and overheads
category_dict = {}

#To remove headers category and overheads from raw data
is_header = True

#Visual Studio Code application requires path of CSV file to be specified
#Path of CSV file
path = "C:/Users/Miko Lee/OneDrive - Ngee Ann Polytechnic/Year 1/PFB/"
#To open CSV file
datafile = open(path + "overheads-day-90.csv", 'r')

#For loops to remove headers category and overheads from raw data
for line in datafile:
    if is_header:
        is_header = False
        continue
    #To remove ]'\n' in data from csv
    line = line.strip('\n')

    #To split data with ','
    line_data = line.split(',')

    #combines line_data[1] into category_dict
    category_dict[line_data[0]] = line_data[1]

    #Test if line_data contains correct information
    #line_data[0] = key e.g. category
    #line_data[1] = value e.g. overheads
    #print(line_data)

    #Using for loop to add values of overheads into overhead_list
    for x in range(0,1):
        
        overhead_list.append(line_data[1])

#Finds the largest float using lambda        
max_overhead = max(overhead_list,key=lambda x:float(x))

#prints the category with the largest overhead in the list
print("{} has the largest overhead of {}".format(list(category_dict.keys())[list(category_dict.values()).index(max_overhead)], max_overhead))

datafile.close()
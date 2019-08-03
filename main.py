import json
import matplotlib.pyplot as plt
import numpy as np

# Load the json file
with open('work_test.json','r') as f:
    example_dict = json.load(f)

# Print the json file to check the value
for example in example_dict:
    print (example)

# Make a copy of the json dictionary    
example_dict_copy = example_dict.copy()

# Convert the string format of the value into the int format from the json dictionary
example_value_list = []
for example in example_dict:
    example_value_list.append(int(example['value']))

# Convert the string format of the time into the int format from the json dictionary    
example_time_list = []
for example in example_dict:
    example_time_list.append(int(example['time']))

##########################Begin Unfiltered Processing################################
# Calculate the unfiltered mean and average number of the value
example_dict_copy_mean = np.mean(example_value_list)
print ("The unfilerted mean and average number is: ",example_dict_copy_mean)

# Calculate the unfiltered minimum number of the value
example_dict_copy_minimum = np.amin(example_value_list)
print ("The unfiltered minimum number is: ",example_dict_copy_minimum)

# Append the unfiltered mean and average number into a list
example_dict_copy_mean_list = []
for i in range(len(example_dict_copy)):
    example_dict_copy_mean_list.append(example_dict_copy_mean)

# Append the unfiltered minimum number into a list
example_dict_copy_minimum_list = []
for i in range(len(example_dict_copy)):
    example_dict_copy_minimum_list.append(example_dict_copy_minimum)
    
#Output the unfiltered figure
plt.figure(figsize=(12,8))
plt.title('The unfiltered figure')
plt.plot(example_time_list,example_dict_copy_minimum_list, c='r', label="Unfiltered Minimum")
plt.plot(example_time_list,example_dict_copy_mean_list, c='b', label="Unfiltered Mean and Average")
plt.legend(loc='best')
plt.show()
##########################End Unfiltered Processing################################

##########################Begin filtered Processing################################
#The filter condition is to filter out the mean and average and minimum number after 2000 year.
# Pick the value after 2000 year
example_value_list_filtered = []
for example in example_dict:
    if int(example["time"]) > 2000 or int(example["time"]) == 2000:
        example_value_list_filtered.append(int(example['value']))
        print (example['value'])

# Pick the time after 2000 year
example_time_list_filtered = []
for example in example_time_list:
    if example > 2000 or example == 2000:
        example_time_list_filtered.append(example)
        print (example)

# Calculate the unfiltered mean and average number of the value
example_dict_copy_mean = np.mean(example_value_list_filtered)
print ("The filtered mean and average number after 2000 year is: ",example_dict_copy_mean)

# Calculate the unfiltered minimum number of the value
example_dict_copy_minimum = np.amin(example_value_list_filtered)
print ("The filtered minimum number after 2000 year is: ",example_dict_copy_minimum)

# Append the unfiltered mean and average number into a list
example_dict_copy_mean_list = []
for i in range(len(example_value_list_filtered)):
    example_dict_copy_mean_list.append(example_dict_copy_mean)

# Append the unfiltered minimum number into a list
example_dict_copy_minimum_list = []
for i in range(len(example_time_list_filtered)):
    example_dict_copy_minimum_list.append(example_dict_copy_minimum)
    
#Output the unfiltered figure
plt.figure(figsize=(12,8))
plt.title('The filtered figure')
plt.plot(example_time_list_filtered,example_dict_copy_minimum_list, c='r', label="filtered Minimum")
plt.plot(example_time_list_filtered,example_dict_copy_mean_list, c='b', label="filtered Mean and Average")
plt.legend(loc='best')
plt.show()
##########################End filtered Processing################################
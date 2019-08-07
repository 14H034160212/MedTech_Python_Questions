import matplotlib.pyplot as plt
import numpy as np


#########begin load json file and transfer the string value into the int value################
def json_string2int(example_dict):
    # Print the json file to check the value
    for example in example_dict:
        print (example)
    
    # Convert the string format of the value into the int format from the json dictionary
    example_value_list = []
    for example in example_dict:
        example_value_list.append(example['value'])
    
    # Convert the string format of the time into the int format from the json dictionary    
    example_time_list = []
    for example in example_dict:
        example_time_list.append(example['time'])
    
    return example_value_list, example_time_list
#########end load json file and transfer the string value into the int value################

##########################Begin Unfiltered Processing################################
def unfilter_processing(example_dict):
    # Calculate the unfiltered mean and average number of the value
    example_value_list, example_time_list = json_string2int(example_dict)
    # Make a copy of the json dictionary    
    example_dict_copy = example_dict.copy()
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
    draw_figure(12,8,'The unfiltered figure',example_time_list,example_dict_copy_minimum_list, example_dict_copy_mean_list,'r','b',"Unfiltered Minimum","Unfiltered Mean and Average",'best')

##########################End Unfiltered Processing################################

##########################Begin filtered Processing with begin and end year ################################
# The filter condition is to filter out the mean and average and minimum number between the begin year and the end year. 
def filter_processing_begin_end(example_dict, begin_year, end_year):
    example_value_list, example_time_list = json_string2int(example_dict)
    # Pick the value after begin_year
    example_value_list_filtered = []
    for example in example_dict:
        if (int(example["time"]) > begin_year or int(example["time"]) == begin_year) and (int(example["time"]) < end_year or int(example["time"]) == end_year):
            example_value_list_filtered.append(int(example['value']))
            print (example['value'])
    
    # Pick the time after begin_year
    example_time_list_filtered = []
    for example in example_time_list:
        if (example > begin_year or example == begin_year) and (example < end_year or example == end_year):
            example_time_list_filtered.append(example)
            print (example)
    
    # Calculate the filtered mean and average number of the value
    example_dict_copy_mean = np.mean(example_value_list_filtered)
    print ("The filtered mean and average number between "+str(begin_year)+ " and " +str(end_year)+ " is: ",example_dict_copy_mean)
    
    # Calculate the filtered minimum number of the value
    example_dict_copy_minimum = np.amin(example_value_list_filtered)
    print ("The filtered minimum number between "+str(begin_year)+ " and " +str(end_year)+ " is: ",example_dict_copy_minimum)
    
    # Append the filtered mean and average number into a list
    example_dict_copy_mean_list = []
    for i in range(len(example_value_list_filtered)):
        example_dict_copy_mean_list.append(example_dict_copy_mean)
    
    # Append the filtered minimum number into a list
    example_dict_copy_minimum_list = []
    for i in range(len(example_time_list_filtered)):
        example_dict_copy_minimum_list.append(example_dict_copy_minimum)
        
    #Output the filtered figure
    draw_figure(12,8,'The filtered figure between '+str(begin_year)+' and '+str(end_year),example_time_list_filtered,example_dict_copy_minimum_list, example_dict_copy_mean_list,'r','b',"filtered Minimum","filtered Mean and Average",'best')
  
##########################End filtered Processing with begin and end year ################################

##########################Begin filtered Processing with only begin year ################################

#The filter condition is to filter out the mean and average and minimum number after the begin year.
def filter_processing_begin(example_dict, begin_year):
    example_value_list, example_time_list = json_string2int(example_dict)
    # Pick the value after begin_year
    example_value_list_filtered = []
    for example in example_dict:
        if int(example["time"]) > begin_year or int(example["time"]) == begin_year:
            example_value_list_filtered.append(int(example['value']))
            print (example['value'])
    
    # Pick the time after begin_year
    example_time_list_filtered = []
    for example in example_time_list:
        if example > begin_year or example == begin_year:
            example_time_list_filtered.append(example)
            print (example)
    
    # Calculate the filtered mean and average number of the value
    example_dict_copy_mean = np.mean(example_value_list_filtered)
    print ("The filtered mean and average number after "+ str(begin_year)+ " year is: ",example_dict_copy_mean)
    
    # Calculate the filtered minimum number of the value
    example_dict_copy_minimum = np.amin(example_value_list_filtered)
    print ("The filtered minimum number after "+ str(begin_year)+ " year is: ",example_dict_copy_minimum)
    
    # Append the filtered mean and average number into a list
    example_dict_copy_mean_list = []
    for i in range(len(example_value_list_filtered)):
        example_dict_copy_mean_list.append(example_dict_copy_mean)
    
    # Append the filtered minimum number into a list
    example_dict_copy_minimum_list = []
    for i in range(len(example_time_list_filtered)):
        example_dict_copy_minimum_list.append(example_dict_copy_minimum)
        
    #Output the filtered figure
    draw_figure(12,8,'The filtered figure after '+str(begin_year),example_time_list_filtered,example_dict_copy_minimum_list, example_dict_copy_mean_list,'r','b',"filtered Minimum","filtered Mean and Average",'best')

##########################End filtered Processing with only begin year ################################
    
########Draw plot program##############
def draw_figure(x,y,title,example_time_list_filtered, example_dict_copy_minimum_list, example_dict_copy_mean_list, color_mini, color_mean, label_mini, label_mean, fig_loc):
    #Output the filtered figure
    plt.figure(figsize=(x,y))
    plt.title(title)
    plt.plot(example_time_list_filtered,example_dict_copy_minimum_list, c=color_mini, label=label_mini)
    plt.plot(example_time_list_filtered,example_dict_copy_mean_list, c=color_mean, label=label_mean)
    plt.legend(loc=fig_loc)
    plt.show() 
########Draw plot program##############
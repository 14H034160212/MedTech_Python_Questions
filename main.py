import json
from methods import unfilter_processing, filter_processing_begin_end, filter_processing_begin

if __name__ == '__main__':
    # Load the json file
    with open('work_test.json','r') as f:
        example_dict = json.load(f)

    # Print the unfilter result
    unfilter_processing(example_dict)
    
    # Print the filter result with begin and end year
    begin_year=2000
    end_year=2010
    filter_processing_begin_end(example_dict, begin_year, end_year)
    
    # Print the filter result with only begin year
    begin_year=2001
    filter_processing_begin(example_dict, begin_year)
  
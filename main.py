import sys
import CsvToList
import descriptive_stats

original_stdout = sys.stdout


# 0 indicates csv file contains events
# 1 indicates csv file contains object-value
events_var = 0
objects_var = 1

events_filename = input("Enter the name of the csv file containing Event times: ")
objects_filename = input("Enter the name of the csv file containing an Object | Value: ")


events_list = CsvToList.parse_csv_file(0, events_filename)
objects_list = CsvToList.parse_csv_file(1, objects_filename)




events = descriptive_stats.DescriptiveStats(events_list, events_var)
objects = descriptive_stats.DescriptiveStats(objects_list, objects_var)



events.create_graphs(events.data, events_var)
objects.create_graphs(objects.data, objects_var)

with open('frequency_events.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    events.print_data()
    sys.stdout = original_stdout

with open('frequency_lengths.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    objects.print_data()
    sys.stdout = original_stdout


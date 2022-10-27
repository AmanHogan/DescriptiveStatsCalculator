import sys
import csv_to_list as ctl
import stats_calc as stats

original_stdout = sys.stdout

# 0 indicates csv file contains events
# 1 indicates csv file contains object-value
events_var = 0
objects_var = 1

# retrieve filename of csv
events_filename = input("Enter the name of the csv file containing Event times: ")
event_graph_name = input(f"Enter the desired graph title for {events_filename}: ")

objects_filename = input("Enter the name of the csv file containing an Object | Value: ")
object_graph_name = input(f"Enter the desired graph titles for {objects_filename}: ")

# get list of events or list of objects
events_list = ctl.parse_csv_file(0, events_filename)
objects_list = ctl.parse_csv_file(1, objects_filename)

# create object to store descriptive statistics
events = stats.DescriptiveStats(events_list, events_var)
objects = stats.DescriptiveStats(objects_list, objects_var)

# create graphs from the data
events.create_graphs(events.data, events_var, event_graph_name)
objects.create_graphs(objects.data, objects_var, object_graph_name)

# save a file containing the descriptive statistics
with open('events_freq_table.txt', 'w') as f:
    sys.stdout = f  # Change the standard output to the file we created.
    events.print_data()
    sys.stdout = original_stdout

with open('objects_freq_table.txt', 'w') as f:
    sys.stdout = f  # Change the standard output to the file we created.
    objects.print_data()
    sys.stdout = original_stdout

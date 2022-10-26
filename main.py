import sys
import FormatCsv
import descriptive_stats

original_stdout = sys.stdout
list_of_events = FormatCsv.parse_csv_file(0)
list_of_objects = FormatCsv.parse_csv_file(1)


# var indicates a file contains events
event_time = 0

# var indicates a file contains object-value
object_value = 1

events = descriptive_stats.DescriptiveStats(list_of_events, event_time)
objects = descriptive_stats.DescriptiveStats(list_of_objects, object_value)



events.create_graphs(events.data, event_time)
objects.create_graphs(objects.data, object_value)

with open('frequency_events.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    events.print_data()
    sys.stdout = original_stdout

with open('frequency_lengths.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    objects.print_data()
    sys.stdout = original_stdout


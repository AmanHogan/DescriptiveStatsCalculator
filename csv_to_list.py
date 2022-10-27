import csv


##################################################################
# FUNCTION: find_inter_arrival_time(time1, time2)
# Finds the difference between time2 and time1 (inter-arrival time)
#   PARAMS:
#       time1 - the previous time listed in csv file
#       time2 - the current time listed in the csv file
#   RETURNS:
#      delta_t - difference in seconds of time2 and time1
#
##################################################################
def find_inter_arrival_time(time1, time2):
    # get the string time of event 1 and event 2
    # remove the colon from the time
    time1 = str(time1)
    time2 = str(time2)
    time1_str = time1.split(":")
    time2_str = time2.split(":")

    # turn the HH : MM : SS into integers
    h1 = int(time1_str[0])
    h2 = int(time2_str[0])
    m1 = int(time1_str[1])
    m2 = int(time2_str[1])
    s1 = int(time1_str[2])
    s2 = int(time2_str[2])

    # convert HH and MM into seconds
    h1 = h1 * 60 * 60
    h2 = h2 * 60 * 60
    m1 = m1 * 60
    m2 = m2 * 60

    # return the difference between time1 and time2
    t1_total = h1 + m1 + s1
    t2_total = h2 + m2 + s2
    delta_t = t2_total - t1_total

    return delta_t


#########################################################################
# FUNCTION: parse_csv_file(event_or_object, filename)
# Converts csv data into a list and returns this list
#   PARAMS:
#       event_or_object - 0 or 1 whether csv has events or object | value
#       filename - name of file to be parsed
#   RETURNS:
#      list_of_events | list_of_objects - list of the data in csv
#
#########################################################################
def parse_csv_file(event_or_object, filename):
    # the file to be parsed is an event
    if event_or_object == 0:

        # Parse the csv file
        with open(filename, "r") as f:
            csv_reader = csv.DictReader(f, fieldnames=["Event", "Time"])
            list_of_events = list(csv_reader)

            # for each row, calculate the inter-arrival time and
            # input it into a new column called Time
            for i in range(len(list_of_events)):
                if i == 0:
                    continue

                diff = find_inter_arrival_time(list_of_events[i - 1].get("Event"), list_of_events[i].get("Event"))
                list_of_events[i]["Time"] = diff

        return list_of_events

    # the file to be parsed is an object | value
    elif event_or_object == 1:

        # Parse the csv file
        with open(filename, "r") as f:
            csv_reader = csv.DictReader(f, fieldnames=["Object", "Length"])
            list_of_objects = list(csv_reader)

            # convert each key value into an integer
            for obj in list_of_objects:
                for keys in obj:
                    obj[keys] = int(obj[keys])

        return list_of_objects

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


def parse_csv_file(event_or_object):

    # the file to be parsed is an event
    if event_or_object == 0:
        with open("Event_Arrival.csv", "r") as f:
            csv_reader = csv.DictReader(f, fieldnames=["Event", "Time"])
            events = list(csv_reader)

            for i in range(len(events)):
                if i == 0:
                    continue
                diff = find_inter_arrival_time(events[i - 1].get("Event"), events[i].get("Event"))
                events[i]["Time"] = diff
        return events

    elif event_or_object == 1:
        with open("Length_of_Rivers.csv", "r") as f:
            csv_reader = csv.DictReader(f, fieldnames=["Object", "Length"])
            objects = list(csv_reader)
            for obj in objects:
                for keys in obj:
                    obj[keys] = int(obj[keys])
        return objects

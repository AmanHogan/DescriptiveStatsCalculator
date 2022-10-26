import csv

debug = 1

def find_diff(event1, event2):
    event1 = str(event1)
    event2 = str(event2)

    parsed_event_1 = event1.split(":")
    parsed_event_2 = event2.split(":")

    h1 = int(parsed_event_1[0])
    m1 = int(parsed_event_1[1])
    s1 = int(parsed_event_1[2])

    h2 = int(parsed_event_2[0])
    m2 = int(parsed_event_2[1])
    s2 = int(parsed_event_2[2])

    h1 = h1 * 60 * 60
    h2 = h2 * 60 * 60

    m1 = m1 * 60
    m2 = m2 * 60

    total_seconds_e1 = h1 + m1 + s1
    total_seconds_e2 = h2 + m2 + s2
    total_difference = total_seconds_e2 - total_seconds_e1

    return total_difference

def parse_csv_file(num):
    if num == 0:
        with open("Event_Arrival.csv", "r") as f:
            csv_reader = csv.DictReader(f, fieldnames=["Event", "Time"])
            events = list(csv_reader)

            for i in range(len(events)):
                if i == 0:
                    continue
                diff = find_diff(events[i - 1].get("Event"), events[i].get("Event"))
                events[i]["Time"] = diff
        return events

    elif num == 1:
        with open("Length_of_Rivers.csv", "r") as f:
            csv_reader = csv.DictReader(f, fieldnames=["Object", "Length"])
            objects = list(csv_reader)
            for obj in objects:
                for keys in obj:
                    obj[keys] = int(obj[keys])
        return objects







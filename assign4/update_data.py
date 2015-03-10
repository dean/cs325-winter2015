import sys
import csv
from datetime import datetime


def convert_to_temp(temp):
    temp = float(temp) / 10.0
    return round(temp, 2)


def get_avg_temp(tmax, tmin):
    avg = (tmax + tmin) / 2
    return round(avg, 2)


def get_data(reader):
    rows = []
    first_day = None
    for row in reader:
        curr_day = datetime.strptime(row[-3], "%Y%m%d")
        if first_day is None:
            first_day = curr_day

        tmax, tmin = map(convert_to_temp, row[-2:])
        avg = get_avg_temp(tmax, tmin)
        delta = curr_day - first_day
        row.append(avg)
        row.append(delta.days)
        rows.append(row)
    return rows


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Please provide an input and output file name"
        exit(1)

    header = None
    rows = []
    with open(sys.argv[1], 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = reader.next()
        rows = get_data(reader)
        header.append("average")
        header.append("day")

    with open(sys.argv[2], "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(header)
        writer.writerows(rows)

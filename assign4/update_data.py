import sys
import csv


def get_data(reader):
    rows = []
    first_day = None
    for row in reader:
        curr_day = int(row[-3])
        if first_day is None:
            first_day = curr_day

        tmax, tmin = row[-2:]
        avg = (float(tmax)-float(tmin))/2
        day = curr_day - first_day
        row.append(avg)
        row.append(day)
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

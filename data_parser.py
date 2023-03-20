"""
    # point of this parsing is to create conscise model of data
    # that would be ultimateley saved to csv file
    # row should be represented like this
    # draw_number,draw_day_of_the_week,draw_date,nr1,nr2,nr3,nr4,nr5,nr6
    # 3835,Sobota,05.01.2002,11,27,31,34,39,43
"""
import re
import json
import time
import csv


def parse_using_regex(line: str) -> str:
    """
    define and compalie the search pattern
    locate searched pattern occurance in string below
    https://regex101.com/
    "Czwartek, 10.11.2022, godz. 22:00\nWygrane\nLotto\n6803\n6\n11\n16\n31\n33\n45\nLotto Plus\n6803\n3\n6\n26\n33\n42\n43\nSuper Szansa\n4696\n9\n0\n2\n1\n8\n7\n2"
    """
    search_pattern = re.compile(
        "(.*), (\d+)\.(\d+)\.(\d+).*\\nWygrane\\nLotto\\n(\d+)\\n(\d+)\\n(\d+)\\n(\d+)\\n(\d+)\\n(\d+)\\n(\d+)"
    )
    finding = search_pattern.search(line)
    print(finding)
    result = "No match"

    if finding:
        result = ",".join(map(str, [finding.group(i) for i in range(1, 12)]))

    return result


def save_to_csv(
    lst: list,
):
    with open("unclear_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for i in lst:
            writer.writerow([i])


def parse_draw_data(lst: list):
    """
    using pandas clear the data by droping unnecessery columns
    and fixing the visible problems
    first by looking up the structure of the data frame using .describe()

    """


def main():
    # start measuring time
    start_time = time.time()

    data_dict = {}
    rows_list = []
    with open(f"lotto_data.json", "r", encoding="utf-8") as d:
        data_dict = json.load(d)
    i = 0
    for row in data_dict:
        i = i + 1
        rows_list.append(parse_using_regex(data_dict[str(i)]))

    # add description to csv by inserting it on the firt position
    description = (
        "day_of_the_week,day,month,year,draw_id_number,nr1,nr2,nr3,nr4,nr5,nr6"
    )
    rows_list.insert(0, description)
    save_to_csv(rows_list)

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()

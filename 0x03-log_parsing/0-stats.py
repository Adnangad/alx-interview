#!/usr/bin/python3
"""This module contains func that read input line by line and comp metrics"""
import re
import sys


def print_info(file_size, count_stats):
    """
    Args:
    file_size: sum of file size input
    count_stats: dict that contains status codes
    """
    print(f"File size: {file_size}")
    for stats in sorted(count_stats.keys()):
        if count_stats[stats] > 0:
            print(f"{stats}: {count_stats[stats]}")


def main():
    """
    Executes the whole of the above func
    """
    count = 0
    count_stats = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    file_size = 0
    pattern = re.compile(
    r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] "GET /projects/260 HTTP/1.1" \d{3} \d+$'
    )
    try:
        for line in sys.stdin:
            count = count + 1
            if not pattern.match(line):
                continue
            line = line.split()
            stat_code = int(line[-2])
            file_size += int(line[-1])
            if stat_code in count_stats:
                count_stats[stat_code] += 1
            if count % 10 == 0:
                print_info(file_size, count_stats)
        print_info(file_size, count_stats)
    except KeyboardInterrupt:
        print_info(file_size, count_stats)
        raise


if __name__ == '__main__':
    main()

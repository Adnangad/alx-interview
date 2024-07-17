#!/usr/bin/python3
"""This module contains func that read input line by line and comp metrics"""
from functools import partial
import signal
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


def handler(signum, frame, file_size, count_stats):
    """
    Args:
    signum: the signal
    frame: position in the framework where the signal was called
    file_size: sum of files
    count_stats: dict that contains status codes
    """
    print_info(file_size, count_stats)


def main():
    """
    Executes the whole of the above func
    """
    count = 0
    stat_num = 0
    count_stats = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    file_size = 0
    pattern = re.compile(
    r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] "GET /projects/260 HTTP/1.1" \d{3} \d+$'
    )
    for line in sys.stdin:
        signal.signal(
                signal.SIGINT,
                partial(handler, file_size=file_size, count_stats=count_stats))
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


if __name__ == '__main__':
    main()

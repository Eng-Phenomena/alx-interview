#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics'''

import sys

status_counter = {'200': 0, '301': 0, '400': 0, '401': 0,
                  '403': 0, '404': 0, '405': 0, '500': 0}
total_bytes = 0
line_counter = 0

try:
    for input_line in sys.stdin:
        components = input_line.split()

        if len(components) > 4:
            status_code = components[-2]
            byte_size = int(components[-1])

            if status_code in status_counter:
                status_counter[status_code] += 1

            total_bytes += byte_size
            line_counter += 1

        if line_counter == 10:
            print('File size:', total_bytes)
            for code, count in sorted(status_counter.items()):
                if count > 0:
                    print(f'{code}: {count}')
            line_counter = 0

except Exception as error:
    pass

finally:
    print('File size:', total_bytes)
    for code, count in sorted(status_counter.items()):
        if count > 0:
            print(f'{code}: {count}')

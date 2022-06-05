import datetime
import re


monthes = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
reg1 = re.compile(r"""( # <remote_addr>
                        (?P<ipv4>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
                        |
                        (?P<ipv6>[0-9a-f]{0,4}:[0-9a-f]{0,4}:[0-9a-f]{0,4}:[0-9a-f]{0,4}:[0-9a-f]{0,4}:[0-9a-f]{0,4}:[0-9a-f]{0,4}:[0-9a-f]{0,4})
                      )\s-\s-\s\[
                        # <request_datetime>
                        (?P<day>\d{1,2})\/(?P<month>\w{3})\/(?P<year>\d{4}):(?P<hours>\d{2}):(?P<minutes>\d{2}):(?P<seconds>\d{2})\s(?P<timezone>[\+-]\d{4})
                        \]\s\"
                        # <request_type>
                        (?P<req_type>get|post|head)\s
                        # <requested_resource>
                        (?P<resource>(\/\w+)+)
                        \sHTTP\/1\.1\"\s
                        # <response_code>, <response_size>
                        (?P<resp_code>\d{3})\s(?P<resp_size>\d+)\s""", re.IGNORECASE | re.VERBOSE)



def parse_line(line):
    res = {}

    groups = re.search(reg1, line)
    if groups is None: raise ValueError

    groups = groups.groupdict()
    year = int(groups['year'])
    month = monthes.index(groups['month']) + 1
    day = int(groups['day'])
    hours = int(groups['hours'])
    minutes = int(groups['minutes'])
    seconds = int(groups['seconds'])
    res['remote_addr'] = groups['ipv4'] if groups['ipv4'] else groups['ipv6']
    res['request_datetime'] = datetime.datetime(year, month, day, hours, minutes, seconds)
    res['request_type'] = groups['req_type']
    res['requested_resource'] = groups['resource']
    res['response_code'] = groups['resp_code']
    res['response_size'] = groups['resp_size']

    return res


if __name__ == '__main__':
    with open('task_2/nginx_logs.txt', mode='rt', encoding='UTF-8') as f:
        for line in f:
            try:
                print(parse_line(line))
            except ValueError:
                print('Невозможно разобрать строку')

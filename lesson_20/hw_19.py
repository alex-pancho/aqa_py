from lession_10 import hw_10_logger as l
from pathlib import Path
from datetime import datetime

PATH = Path(__file__).parent / "hblog.txt"


def get_heartbeat(file=PATH) -> dict:
    """
    Receives path to txt file then processing it
    Returns dict where key is flow key and value is
    list with heart beat time values
    """
    with file.open('r') as file:
        result_dict = {}
        try:
            for row in file:
                row = row.split()
                key = row[12]
                time = row[10]
                if key in result_dict:
                    result_dict[key].append(time)
                else:
                    result_dict[key] = [time]
        except KeyError:
            l.logger.error("Process key value is missed")
    return result_dict


def heartbeat_analysis(data_dict):
    """
    Receives data dict with Process key and heartbeat time values
    then calculate heartbeat time difference.
    """
    prev_time = None
    for key, values in data_dict.items():
        for value in values[::-1]:
            try:
                if prev_time is not None:
                    time_diff = (datetime.strptime(value, '%H:%M:%S') - datetime.strptime(prev_time,
                                                                                          '%H:%M:%S')).total_seconds()
                    if 30 < time_diff < 32:
                        l.logger.warning(f'Heartbeat exceeds 30 sec. Process key: {key}, Time: {value}')
                    elif time_diff >= 32:
                        l.logger.error(f'Heartbeat exceeds 31 sec. Process key: {key}, Time: {value}')
                prev_time = value
            except ValueError:
                l.logger.error("Incorrect time value received")


heartbeat_analysis(data_dict=get_heartbeat())

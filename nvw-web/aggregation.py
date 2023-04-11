import csv
import os
from collections import OrderedDict, defaultdict


def list_subdirs(a_dir):
    """List immediate subdirectories of a_dir"""
    # https://stackoverflow.com/a/800201
    return [
        name for name in os.listdir(a_dir)
        if os.path.isdir(os.path.join(a_dir, name))
    ]


def format_trepn_name(name, type_):
    """
    Take the name and the type of a measured metric, and return a string
    containing the name and the unit.

    Example input: ('CPU1 Frequency', 'CPU Frequency [kHz]').
    Example output: 'CPU1 Frequency [kHz]'.
    """
    if '[' in type_:
        unit = ' [' + type_.split('[')[1]
    else:
        unit = ''

    return name + unit


def aggregate_trepn(trepn_logs_dir):
    """
    Aggregate the results of multiple Trepn runs.

    Take average results from all Trepn results in `trepn_logs_dir`,
    and return average values for all metrics in those results.

    The return value looks like this:
    {
        'CPU1 Frequency [kHz]': 954,12,
        'CPU2 Frequency [kHz]': 111,99,
        ...
    }
    """
    log_file_paths = [
        os.path.join(trepn_logs_dir, f)
        for f in os.listdir(trepn_logs_dir)
        if os.path.isfile(os.path.join(trepn_logs_dir, f))
    ]

    # A dictionary collecting all average results per measured metric.
    # Keys are 2-tuples in this form: (name, type).
    runs = defaultdict(list)

    for log_file_path in log_file_paths:
        with open(log_file_path, 'r') as log_file:

            # Read the whole log file into memory. It includes both
            # the detailed part and the aggregated part.
            contents = log_file.read()

            # Take only the aggregated part and remove the "System Statistics" header
            raw_system_stats = contents.split('System Statistics:')[1]

            # Split the rest of the aggregated statistics into lines.
            # The first line is a valid CSV header.
            system_stats = raw_system_stats.strip().splitlines()
            reader = csv.DictReader(system_stats)

            for row in reader:
                run_key = (row['Name'], row['Type'])
                runs[run_key].append(float(row['Average']))

    # Take all average results from `runs` and calculate the averages
    # per measured metric across all runs
    runs_averaged = (
        (format_trepn_name(name, type_), sum(averages) / len(averages))
        for (name, type_), averages in runs.items()
    )

    return OrderedDict(sorted(runs_averaged))


def aggregate_run(data_dir):
    """
    Aggregate a single run.

    To keep the code simple, precisely those properties are aggregated:
    - device,
    - subject,
    - Trepn results (see `aggregate_trepn()`).

    A list of `OrderedDict`s is returned.
    """
    rows = []

    for device in list_subdirs(data_dir):
        device_dir = os.path.join(data_dir, device)

        for subject in list_subdirs(device_dir):
            subject_dir = os.path.join(device_dir, subject)

            for browser in list_subdirs(subject_dir):
                row = OrderedDict((
                    ('device', device),
                    ('subject', subject),
                    ('browser', browser)
                ))

                trepn_dir = os.path.join(subject_dir, browser, 'trepn')
                row.update(aggregate_trepn(trepn_dir))

                rows.append(row)

    return rows


def write_to_file(filename, rows):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def main(device, output_root):
    print('Output root: {}'.format(output_root))

    data_dir = os.path.join(output_root, 'data')
    aggregated_results = aggregate_run(data_dir)

    aggregated_results_path = os.path.join(output_root, 'aggregated_results.csv')
    write_to_file(aggregated_results_path, aggregated_results)

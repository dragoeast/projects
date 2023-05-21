def combine_intervals(intervals):
    """Return the combined intervals.
    >>> intervals = [(1,4), (3,7)]
    >>> combine_intervals(intervals)
    [(1,7)]
    """
    sorted_intervals = sorted(intervals, key=lambda interval: interval[0])

    return combine_intervals(sorted_intervals)

def combine_intervals(sorted_intervals):
    combined_intervals = [ sorted_intervals[0] ]

    for interval in sorted_intervals[1:]:
        last_interval = combined_intervals[-1]
        if interval[0] <= last_interval[-1]:
            end_interval = max(interval[-1], last_interval[-1])
            combined_intervals[-1] = (last_interval[0], end_interval)
        else:
            combined_intervals.append( interval )

    return combined_intervals

intervals = [(1,4), (2,7)]
print(f"{combine_intervals(intervals) = }")

intervals = [ (11,12), (13,15), (1,4), (4,5), (3,6), (10,13) ]
print(f"{combine_intervals(intervals) = }")

from day3.claim import Claim

INPUT_PATH = "input.txt"

# grammar: #{CLAIM_ID} @ {X}, {Y}: {W}x{H}


def main():
    claim_list = get_input()

    # http://tryalgo.org/en/geometry/2016/06/25/union-of-rectangles/
    # https://cp-algorithms.com/data_structures/segment_tree.html
    # https://kartikkukreja.wordpress.com/2014/11/09/a-simple-approach-to-segment-trees/

    # First, divide into y-intervals
    # Then sweep line from left; when line touches the left side of a rect, increment counter(s) for its interval
    # When line leaves the right side, decrement the counter


def calc_elementary_y_intervals(claims):
    """Calculate the elementary y-intervals for a list of claims.

    Basically, just get an ordered list of all the unique y-coords."""
    unique_coords = sorted(list({c.rect.y1 for c in claims} | {c.rect.y2 for c in claims} | {0}))

    if len(unique_coords) % 2:
        unique_coords.append(max(unique_coords)+1)

    intervals,  prev = [], 0
    for i in unique_coords:
        if i == 0:
            continue
        intervals.append(i-prev)
        prev = i

    return tuple(intervals)


def get_input(path=INPUT_PATH):
    with open(path) as f:
        lines = [Claim.from_string(line) for line in f]

    # Invalid lines (blanks) will be None so filter them out
    return [claim for claim in lines if claim is not None]


def get_max_x_value(claim_list):
    return max({x for pair in {(claim.rect.x1, claim.rect.x2) for claim in claim_list} for x in pair})


def find_elementary_intervals(interval_list, y_interval):
    total = 0

    for i, length in enumerate(interval_list):
        total += length
        if total > min(y_interval):
            start = i
            break

    total = 0
    for i, length in enumerate(interval_list):
        total += length
        if total >= max(y_interval):
            end = i
            break

    return start, end


if __name__ == '__main__':
    main()

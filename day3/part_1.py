from itertools import repeat

from day3.claim import Claim
from day3.claim_tree_node import ClaimTreeNode
from tools.segtree import SegmentTree

INPUT_PATH = "input.txt"


def main():
    claim_list = get_input()

    # Find the elementary y-intervals to build our segment tree with
    elementary_y_intervals = calc_elementary_y_intervals(claim_list)

    # Generate the event list from the claims and the elementary intervals
    events = generate_sweep_events(claim_list, elementary_y_intervals)

    # Build the segment tree and iterate it to get our total overlap

    overlap = calculate_overlap(elementary_y_intervals, events)

    print('Number of overlapping squares:', overlap)


def calc_elementary_y_intervals(claims):
    """Calculate the elementary y-intervals for a list of claims.

    Basically, just get an ordered list of all the unique y-coords, then calculate
    the lengths of the intervals between them.

    For the sample data, this should return (1, 2, 2, 2)

    Params:

    claims - Iterable containing Claim objects to process"""
    # Get the union of the sets of top and bottom y-coordinates
    unique_coords = {c.rect.y1 for c in claims} | {c.rect.y2 for c in claims}

    # We already know 0 is the origin so throw it out if it's there
    unique_coords.discard(0)

    # Turn the set into a sorted list
    unique_coords = sorted(list(unique_coords))

    # Subtract the previous item in the list from the current one to get the interval
    # between them.
    intervals,  prev = [], 0
    for i in unique_coords:
        intervals.append(i-prev)
        prev = i

    return tuple(intervals)


def get_input(path=INPUT_PATH):
    """Get the problem input from the data file.

    Reads the file line by line and builds a list by calling the factory method on
    Claim. Invalid claims are filtered out.

    Params:

    path - Path to input file"""
    with open(path) as f:
        lines = [Claim.from_string(line) for line in f]

    # Invalid lines (blanks) will be None so filter them out
    return [claim for claim in lines if claim is not None]


# Given a list of elementary intervals, find which one the given y-interval belongs to
# Called by generate_sweep_events, not by main
def find_segtree_interval(interval_list, y_interval):
    """Find the starting and ending elementary y-interval for the given rectangle y-interval.

    For instance, the sample data is divided into 5 elementary y-intervals: (1, 2, 2, 2, 1).
    The rectangle coordinates in the sample data map to the elementary y-intervals as follows:

    (3, 7) => (2, 3)
    (1, 5) => (1, 2)
    (5, 7) => (3, 3)"""
    total = 0
    start = 0
    end = 0

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


def generate_sweep_events(claim_list, interval_list):
    """Generate the table of events used to sweep the segment tree.

    This is a dictionary where the keys are x-coordinates and the values are lists
    of tuples that each represent a transformation (i.e. the left or right edge of a rect.)"""
    sweep_events = [((c.rect.x1,) + find_segtree_interval(interval_list, (c.rect.y1, c.rect.y2)) + (1,),
                     (c.rect.x2,) + find_segtree_interval(interval_list, (c.rect.y1, c.rect.y2)) + (-1,))
                    for c in claim_list]
    sweep_events = [evt for pair in sweep_events for evt in pair]

    event_dict = {}

    for x, y1, y2, delta in sweep_events:
        if x in event_dict:
            event_dict[x].append((y1, y2, delta))
        else:
            event_dict[x] = [(y1, y2, delta)]

    return event_dict


def calculate_overlap(intervals, events):
    """Calculate the number of square inches where claims overlap.

    Works by initializing a segment tree with the elementary y-intervals, then sweeping it
    from left to right. An interval's value increments when we find the left side of a rectangle
    on it, and decrements when we find the right side. Overlap is the total length of y-intervals
    whose value is >= 2.

    This algorithm caches the last score and x-value and multiplies when there are
    columns with no events.

    Params:

    intervals - The elementary y-intervals for this problem
    events - The event list. See generate_sweep_events"""
    # Initialize the segtree with values set to 0
    segtree = SegmentTree(list(zip(repeat(0), intervals)), ClaimTreeNode)
    total_score = 0
    last_score = total_score
    last_x = 0

    for x, event_list in sorted(events.items()):
        # Update the segment tree with each event at this x-value
        for event in event_list:
            segtree.update(*event)

        # Calculate the score for any rows we skipped over (i.e. no events)
        total_score += last_score * (x - last_x)

        # Save the score and x for this row
        last_x = x
        last_score = segtree.get_score()

    return total_score


if __name__ == '__main__':
    main()

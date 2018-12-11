from day3.claim import Claim
from day3.part_1 import INPUT_PATH


def main():
    claims = get_input()

    unique_claim = find_non_overlapping_claim(claims)

    print('Non-overlapping Claim:', unique_claim)


def get_input(path=INPUT_PATH):
    """Get the problem input from the data file.

    Reads the file line by line and builds a dict by calling the factory method on
    Claim. Invalid claims are filtered out. The keys are the claim IDs.

    Params:

    path - Path to input file"""
    with open(path) as f:
        claims = [Claim.from_string(line) for line in f]

    return {claim.claim_id: claim for claim in claims if claim is not None}


def find_non_overlapping_claim(claims):
    """Find the claim that doesn't overlap any others, if any.

    claims - a dict of claims with claim IDs as keys"""
    for claim_id_1, claim_1 in claims.items():
        for claim_id_2, claim_2 in claims.items():
            # If there's even one overlap, we can stop the inner loop
            if claim_id_1 != claim_id_2 and claim_1.intersects(claim_2):
                break
        else:
            # If iteration completed without breaking, we have a winner
            return claim_id_1

    # If we exhausted all the claims without finding a unique one, there are none
    return None


if __name__ == '__main__':
    main()

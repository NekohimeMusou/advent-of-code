# Sweep Algorithm Visualization

## Sample Data

\#1 @ 1,3: 4x4
\#2 @ 3,1: 4x4
\#3 @ 5,5: 2x2

## Visual

........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........

Sweep at x=0: [0, 0, 0, 0, 0, 0, 0, 0] Evt: None
Sweep at x=1: [0, 0, 0, 1, 1, 1, 1, 0] Evt: x=1, delta=1, interval=[3,6]
Sweep at x=2: [0, 0, 0, 1, 1, 1, 1, 0] Evt: None
Sweep at x=3: [0, 1, 1, 2, 2, 1, 1, 0] Evt: x=3, delta=1, interval=[1,4]
from enum import Enum, auto


class EventType(Enum):
    SHIFT_BEGIN = auto()
    SLEEP = auto()
    WAKE = auto()


class ScheduleEvent:
    def __init__(self, timestamp, guard_id, event_type):
        self.timestamp = timestamp
        self.guard_id = guard_id
        self.type = event_type

    def __eq__(self, other):
        if isinstance(other, ScheduleEvent):
            return self.__dict__ == other.__dict__
        return False

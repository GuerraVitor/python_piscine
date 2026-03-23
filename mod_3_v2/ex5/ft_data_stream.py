import random
from typing import Generator

def gen_event() -> Generator[tuple, None, None]:
    """Infinity generator that produces events on demand."""
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "slep", "move", "climb", "swim", "grab", "release", "use"]

    while True:
        name = random.choice(players)
        action = random.choice(actions)

        yield (name, action)

def consume_event(event_list: list) -> Generator[tuple, None, None]:
    """Generator that empties a list randomly, item by item."""
    while len(event_list) > 0:
        event = random.choice(event_list)
        event_list.remove(event)

        yield event

def main():
    print("=== Game Data Stream Processor ===")
    stream = gen_event()

    for i in range(1001):
        event = next(stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    ten_event_list = []
    for _ in range(10):
        ten_event_list.append(next(stream))

    print(f"Built list of 10 events: {ten_event_list}")

    for event in consume_event(ten_event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_event_list}")

if __name__ == "__main__":
    main()

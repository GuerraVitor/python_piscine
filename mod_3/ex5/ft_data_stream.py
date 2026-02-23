"""Memory-efficient processing using generators to stream and filter data."""

import time
import random


def event_generator(count):
    """Generate events by demmand - lazy evaluation."""
    players = ['alice', 'bob', 'charlie', 'diana', 'eve']
    actions = ['killed monster', 'found treasure',
               'leveled up', 'joined guild']

    for i in range(1, count + 1):
        event = {
            'id': i,
            'player': random.choice(players),
            'level': random.randint(1, 20),
            'action': random.choice(actions),
            'timestamp': time.time()
        }
        yield event


def fibonacci_generator(n):
    """Generate the n firts numbers of Fibonacci sequence."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def prime_generator(n):
    """Generate the firsts n prime numbers."""
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            count += 1
        num += 1


def main():
    """Simulate data stream and process it in real-time using generators."""
    print("=== Game Data Stream Processor ===\n")

    total_events = 1000
    print(f"Processing {total_events} game events...\n")

    stream = event_generator(total_events)
    stats = {
        'high_level': 0,
        'treasure': 0,
        'level_up': 0
    }

    start_time = time.time()

    for event in stream:
        if event['id'] <= 3:
            print(f"Event {event['id']}: PLayer {event['player']}"
                  f"(level {event['level']}) {event['action']}")
        elif event['id'] == 4:
            print("...")

        if event['level'] >= 10:
            stats['high_level'] += 1

        if event['action'] == 'found treasure':
            stats['treasure'] += 1
        elif event['action'] == 'leveled up':
            stats['level_up'] += 1

    end_time = time.time()

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+):{stats['high_level']}")
    print(f"Treasure events: {stats['treasure']}")
    print(f"Level-up events: {stats['level_up']}\n")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {end_time - start_time:.3f} seconds")

    print("\n=== Generator Demonstration ===")

    fib_list = list(fibonacci_generator(10))
    print(f"Fibonacci sequence (first 10): {', '.join(map(str, fib_list))}")

    prime_list = list(prime_generator(5))
    print(f"Prime numbers (first 5): {', '.join(map(str, prime_list))}")


if __name__ == "__main__":
    main()

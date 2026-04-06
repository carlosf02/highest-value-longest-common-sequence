import os
import random

# Fixed alphabet with random values
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f']
VALUES = {ch: random.randint(1, 20) for ch in ALPHABET}

# String lengths for the 10 test files
LENGTHS = [25, 50, 100, 200, 400, 600, 800, 1000, 1500, 2000]

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')


def generate_test(length, filename):
    A = ''.join(random.choice(ALPHABET) for _ in range(length))
    B = ''.join(random.choice(ALPHABET) for _ in range(length))

    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'w') as f:
        f.write(f"{len(ALPHABET)}\n")
        for ch in ALPHABET:
            f.write(f"{ch} {VALUES[ch]}\n")
        f.write(f"{A}\n")
        f.write(f"{B}\n")

    print(f"Created {filename} (length {length})")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for i, length in enumerate(LENGTHS, 1):
        filename = f"test_{i:02d}_len{length}.in"
        generate_test(length, filename)

    print(f"\nGenerated {len(LENGTHS)} test files in data/")


if __name__ == "__main__":
    main()
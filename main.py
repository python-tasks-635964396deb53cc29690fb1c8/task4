from pathlib import Path


def count_pairs_candidate(file: Path) -> int:
    with open(file, 'r', encoding="utf-8") as stream:
        count, barrier = list(map(int, stream.readline().split()))
        nump = int(stream.readline())
        pairs = 0
        for i in range(1, count):
            num = int(stream.readline())
            if nump + num >= barrier:
                pairs += 1
            nump = num
        return pairs


print(count_pairs_candidate(Path('./27-169bb.txt')), end=' ')
print(count_pairs_candidate(Path('./27-169b.txt')))

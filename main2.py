import pickle
import gzip

groups = {}


def add(group: dict):
    musical = input("Enter group: ")
    album = input("Enter album: ")

    group[musical] = album

    return group


def delete_data(group: dict):
    musical = input("Enter group to delete: ")

    group.pop(musical)

    return group


def search(group: dict):
    musical = input("Enter group: ")
    print(f"Album you found: {group[musical]}")


def edit(group: dict):
    album = input("Enter album: ")
    group[album] = input("Enter new capital: ")

    return group


def save(group: dict):
    with gzip.open("newfile.gz", "wb") as f:
        packaged = gzip.compress(pickle.dumps(group))
        f.write(packaged)


def load_data():
    with gzip.open("newfile.gz", "rb") as f:
        compressed = f.read()

    decompressed = gzip.decompress(compressed)
    new1 = pickle.loads(decompressed)
    return new1


groups = add(groups)
groups = add(groups)

print(groups)

groups = edit(groups)

print(groups)

save(groups)

new = load_data()

print(new)

import pickle
import gzip

countries = {}


def add(countries_par: dict):
    country = input("Enter country: ")
    capital = input("Enter capital: ")

    countries_par[country] = capital

    return countries_par


def delete_data(countries_par: dict):
    country = input("Enter country to delete: ")

    countries_par.pop(country)

    return countries_par


def search(countries_par: dict):
    country = input("Enter country: ")
    print(f"Capital you found: {countries_par[country]}")


def edit(countries_par: dict):
    country = input("Enter country: ")
    countries_par[country] = input("Enter new capital: ")

    return countries_par


def save(countries_par: dict):
    with gzip.open("newfile.gz", "wb") as f:
        packaged = gzip.compress(pickle.dumps(countries_par))
        f.write(packaged)


def load_data():
    with gzip.open("newfile.gz", "rb") as f:
        compressed = f.read()

    decompressed = gzip.decompress(compressed)
    new1 = pickle.loads(decompressed)
    return new1


countries = add(countries)
countries = add(countries)

print(countries)

countries = edit(countries)

print(countries)

save(countries)

new = load_data()

print(new)

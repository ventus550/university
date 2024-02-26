# /usr/bin/env python3
import itertools
import pandas
from sklearn.metrics.pairwise import haversine_distances
from math import radians


def distance(row1, row2):
    """Computes the Haversine distance between two towns in the database.
    Source: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.haversine_distances.html"""
    pos1 = (row1['coordinates']['lat'], row1['coordinates']['lon'])
    pos2 = (row2['coordinates']['lat'], row2['coordinates']['lon'])
    radians1 = [radians(pos1[0]), radians(pos1[1])]
    radians2 = [radians(pos2[0]), radians(pos2[1])]
    res = haversine_distances([radians1, radians2])
    res *= 6371000 / 1000  # multiply by Earth radius to get kilometers
    return res[0][1]


# The following is a simple example of parsing the dataset. You are free to extract any subset of the cities
# to benchmark your LP/ILP solutions. You can also transform the dataset into some intermediary data that is
# easier to parse -- for example, creating the distance matrix explicitly, and not just implicitly.

# You are also free to implement the solution in a language other than Python. In that case, please use the same
# dataset, so that the results are somewhat comparable.

# Data source: https://public.opendatasoft.com/explore/dataset/geonames-all-cities-with-a-population-1000/information/?disjunctive.cou_name_en&sort=name

df = pandas.read_json("dataset.json")
print(f"There are {len(df.index)} entries in the file overall.")
europe = df[df['timezone'].str.contains("Europe")]
print(f"There are {len(europe.index)} entries for towns in Europe.")
first_in_europe = europe.iloc[0]
second_in_europe = europe.iloc[-1]
print(f"The distance between {first_in_europe['name']} and {second_in_europe['name']} is "
      f"{distance(first_in_europe, second_in_europe)} km.")

poland = europe[europe['country_code'].str.contains('PL')]
print(f"There are {len(poland.index)} entries for towns in Poland.")
first_in_poland = poland.iloc[0]
second_in_poland = poland.iloc[1]

print(f"The distance between {first_in_poland['name']} and {second_in_poland['name']} is "
      f"{distance(first_in_poland, second_in_poland)} km.")

# The actual distance between Żurowa and Wyśmierzyce seems to be 219 kms, and the function claims 201 km.

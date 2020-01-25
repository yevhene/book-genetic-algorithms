import sys
import csv
import math
from collections import Counter

labels = ['x', 'y', 'in']
data = []

with open(sys.argv[1], newline='') as csvfile:
  reader = csv.reader(csvfile, delimiter=' ')
  for row in reader:
    data.append([int(row[0]), int(row[1]), row[2] == 'True'])

def get_column(data, i):
  return list(map(lambda d: d[i], data))

def entropy(values):
  frequency = Counter(values)
  total = len(values)

  def item_entropy(value):
    ratio = float(frequency[value]) / total
    return -1 * ratio * math.log2(ratio)

  return sum([item_entropy(value) for value in set(values)])

def split(data, feature_index, value):
  left = [item for item in data if item[feature_index] < value]
  right = [item for item in data if item[feature_index] >= value]
  return left, right

def find_split(data):
  feature_indexes = len(data[0]) - 1
  best_entropy = entropy(get_column(data, 2))
  best_feature_index = None
  best_value = None

  def part_entropy(part):
    return entropy(get_column(part, 2)) * (float(len(part)) / len(data))

  for feature_index in range(feature_indexes):
    for value in set(get_column(data, feature_index)):
      left, right = split(data, feature_index, value)
      current_entropy = part_entropy(left) + part_entropy(right)
      if current_entropy < best_entropy:
        best_entropy = current_entropy
        best_feature_index = feature_index
        best_value = value

  return best_feature_index, best_value

def build_tree(data, labels, return_data = False):
  feature_index, value = find_split(data)

  if feature_index is None:
    if return_data:
      return data
    else:
      return None

  left, right = split(data, feature_index, value)
  node = {
    'index': feature_index,
    'feature': labels[feature_index],
    'value': value,
    'left': build_tree(left, labels),
    'right': build_tree(right, labels)
  }

  return node

def represent_tree(tree, prefix=''):
  result = prefix
  if not tree['left'] is None:
    result += f"if {tree['feature']} < {tree['value']}\n"
    result += represent_tree(tree['left'], prefix + '  ')
  if not tree['right'] is None:
    result += f"if {tree['feature']} >= {tree['value']}\n"
    result += represent_tree(tree['right'], prefix + '  ')
  return result

tree = build_tree(data, labels)
print(represent_tree(tree))

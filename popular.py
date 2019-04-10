import json


def install_sort(package):
    return package['analytics']['365d']


with open('package_info.json', 'r') as f:
    data = json.load(f)

# can filter by keyword in the description
data = [item for item in data if 'video' in item['desc']]
data.sort(key=install_sort, reverse=True)

# can take only top 5
# data_str = json.dumps(data[:5], indent=2)
data_str = json.dumps(data, indent=2)
print(data_Str)

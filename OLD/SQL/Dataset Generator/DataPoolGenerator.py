import csv
from faker import Faker
fake = Faker()

data = []
for _ in range(4000):  # Generate 1000 entries for general pool
    entry = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'phone_number': fake.phone_number(),
        'email': fake.email(),
        'address': fake.address().replace('\n', ', ')
    }
    data.append(entry)


keys = data[0].keys()
with open('GeneralPool1.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)


# Generate 100 more for ground truth data
groundTruthData = []
for _ in range(100):
    entry = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'phone_number': fake.phone_number(),
        'email': fake.email(),
        'address': fake.address().replace('\n', ', ')
    }
    groundTruthData.append(entry)

# Save to CSV
keys = groundTruthData[0].keys()
with open('GroundTruth.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(groundTruthData)

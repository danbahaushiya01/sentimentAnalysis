import csv

# Sample data (replace with your actual data)
data = [
    ["Tweet ID", "Tweet Text", "Author Username", "Timestamp"],
    ["12345", "This is a sample tweet.", "user123", "2023-12-31 23:59:59"],
    # ... more rows
]

# Write the data to a CSV file named 'result.csv'
with open('result.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data)

print("result.csv file has been created successfully.")

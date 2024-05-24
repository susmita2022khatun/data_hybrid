import csv

with open('new.txt', 'r') as file:
    lines = file.readlines()

data = []
for i in range(0, len(lines), 4):  
    time = lines[i+1].strip()  
    sensor_read = lines[i+3].strip()[1:-1]  
    data.append({"time": time, "sensor_read": sensor_read})

with open('output.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["time", "sensor_read"])
    writer.writeheader()
    writer.writerows(data)

print("CSV file created successfully.")

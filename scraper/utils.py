import csv

def display_objects(data, object_type):
    print(f"\nFound {object_type}:")
    if data:
        for item in data:
            print(item)
    else:
        print(f"Not found {object_type}.")
        
def save_data(data):
    if not data:
        print("There is no data to save.")
        return
    
    filename = input("Enter a name for the file to save (eg.: 'data.csv'): ")
    keys = data[0].keys() if isinstance(data, list) else ['data']
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if isinstance(data, list) and keys != ['data']:
            writer.writerow(keys)
            for row in data:
                writer.writerow(row.values())
        else:
            writer.writerow(data)
            for row in data:
                writer.writerow([row])
    print(f"The data has been saved successfully to {filename}.")
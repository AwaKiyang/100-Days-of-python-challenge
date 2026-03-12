import csv

class csv_data:
    """
    class reponsible for reading and write to the csv file
    """
    def __init__(self):
        pass

    def data_reader():
        """
        Method used to read csv file and obtain its data
        """
        with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
            csv_data = list(csv.reader(csv_file, delimiter=','))
            csv_data.pop(0)
            return csv_data
        
    def data_writer(row):
        """
        Method used to write data to csv
        """
        with open('cafe-data.csv', "a", newline="", encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)        # Create writer object
            return csvwriter.writerow(row)              # Write multiple rows

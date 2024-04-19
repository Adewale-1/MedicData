

import csv

class WriteCsvFile:
    def __init__(self, file_path, first_name, last_name, email, error):
        self.file_path = file_path
        self.header = ['First Name', 'Last Name', 'Email', 'Error']
        self.email = email
        self.error = error
        self.first_name = first_name
        self.last_name = last_name
        
    def write_csv_file(self):
        # The data to be written to the CSV file
        data = [self.first_name, self.last_name, self.email, self.error]

        # Open the file in append mode, 'a', so that we don't overwrite the existing data
        with open(self.file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # Check if the file is empty to decide whether to write the header
            if file.tell() == 0:
                writer.writerow(self.header)
            
            # Write the data row to the CSV file
            writer.writerow(data)


    
import random
import string
#import sqlite3
import csv

def generate_test_data(table_name, column_names, column_types, num_rows, output_file):
    # Generate test data
    rows = []
    for i in range(num_rows):
        row = []
        for j in range(len(column_names)):
            column_type = column_types[j].split("(")[0]
            if column_type == "INT":
                row.append(random.randint(0, 1000))
            elif column_type == "VARCHAR":
                row.append(''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(1, 50))))
            elif column_type == "DECIMAL":
                precision = int(column_types[j].split(",")[0].split("(")[1])
                scale = int(column_types[j].split(",")[1].split(")")[0])
                row.append(round(random.uniform(0, 1000), scale))
            elif column_type == "TIMESTAMP":
                row.append("2022-05-01 00:00:00")
        rows.append(row)

    # Write test data to CSV file
    with open(output_file, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(column_names)
        for row in rows:
            writer.writerow(row)

    print(f"Generated {num_rows} rows of test data for table {table_name} and wrote it to {output_file}")

# Example usage
table_name = "sales"
column_names = ["transaction_id", "customer_id", "transaction_date", "product_name", "unit_price", "quantity", "total_amount"]
column_types = ["INT", "INT", "TIMESTAMP", "VARCHAR(50)", "DECIMAL(10,2)", "INT", "DECIMAL(10,2)"]
num_rows = 100000
output_file = "sales_data.csv"

generate_test_data(table_name, column_names, column_types, num_rows, output_file)



''' 
Below set of code for creating inmemory table
def generate_test_data(table_name, column_names, column_types, num_rows):
    # Create database connection and cursor
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()

    # Generate SQL create table statement
    sql_create_table = f"CREATE TABLE {table_name} ("
    for i in range(len(column_names)):
        sql_create_table += f"{column_names[i]} {column_types[i]},"
    sql_create_table = sql_create_table[:-1] + ")"

    # Create table
    c.execute(sql_create_table)

    # Generate test data and insert into table
    for i in range(num_rows):
        values = []
        for j in range(len(column_names)):
            column_type = column_types[j].split("(")[0]
            if column_type == "INT":
                values.append(random.randint(0, 1000))
            elif column_type == "VARCHAR":
                values.append(''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(1, 50))))
            elif column_type == "DECIMAL":
                precision = int(column_types[j].split(",")[0].split("(")[1])
                scale = int(column_types[j].split(",")[1].split(")")[0])
                values.append(round(random.uniform(0, 1000), scale))
            elif column_type == "TIMESTAMP":
                values.append("2022-05-01 00:00:00")
        sql_insert = f"INSERT INTO {table_name} ({','.join(column_names)}) VALUES ({','.join(['?' for i in range(len(column_names))])})"
        c.execute(sql_insert, values)

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print(f"Generated {num_rows} rows of test data for table {table_name}")

# Example usage
table_name = "sales"
column_names = ["transaction_id", "customer_id", "transaction_date", "product_name", "unit_price", "quantity", "total_amount"]
column_types = ["INT", "INT", "TIMESTAMP", "VARCHAR(50)", "DECIMAL(10,2)", "INT", "DECIMAL(10,2)"]
num_rows = 1000

generate_test_data(table_name, column_names, column_types, num_rows)
'''
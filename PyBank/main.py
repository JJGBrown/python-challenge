import csv
import os

total_months = 0
total_pl = 0
average_change = 0
first_row = None
last_row = None
current_row = None
previous_row = None
greatest_increase = 0
greatest_increase_month = ''
greatest_decrease = 0
greatest_decrease_month = ''


with open('PyBank/Homework_03-Python_PyBank_Resources_budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            if line_count == 1:
                first_row = row
                current_row = row
                previous_row = row
            previous_row = current_row
            current_row = row
            difference =  int(current_row[1]) - int(previous_row[1])
            if greatest_increase < difference:
                greatest_increase = difference
                greatest_increase_month = current_row[0]
            if greatest_decrease > difference:
                greatest_decrease = difference
                greatest_decrease_month = current_row[0]
            line_count += 1
            total_pl += int(row[1])
            last_row = row

    total_months = line_count - 1
    average_change = round((int(last_row[1]) - int(first_row[1])) / (line_count - 1 - 1), 2)

    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_pl}')
    print(f'Average  Change: ${average_change}')
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')
    
    Result = open("PyBank/Result.txt","a")
    Result.write('Financial Analysis\n')
    Result.write('----------------------------\n')
    Result.write(f'Total Months: {total_months}\n')
    Result.write(f'Total: ${total_pl}\n')
    Result.write(f'Average  Change: ${average_change}\n')
    Result.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n')
    Result.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n')
    Result.close()
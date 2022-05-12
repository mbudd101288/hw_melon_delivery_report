

def melon_count(day_number, day_log):
    """Given the day and associated daily log, generate produce report
        
        report will detail produce type, amount, and total price"""
    print("Day", day_number)



    delivery_log = open(day_log)
    for line in delivery_log:
        line = line.rstrip()

        words = line.split('|') 
        # breaks up line into list of strings

        melon = words[0]
        # assign each index in list to variable
        count = float(words[1])
        # convert second index to a float since the count variable should be a number
        amount = float(words[2]) * count
        # conver third index (price of each fruit) to float and calculate total cost 


        print(f"Delivered {count} {melon}s for total of ${amount}")
        # display info using f string

    delivery_log.close()
    
day_1 = melon_count(1, "um-deliveries-day-1.txt")
# call the function using an existing day log report 
# day_2 = melon_count(2, "um-deliveries-day-2.txt")

day_3 = melon_count(3, "um-deliveries-day-3.txt")

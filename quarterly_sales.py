def display_menu ():  
    print("The Quarterly Sales Program")

# gets quarter sales from user
def get_sales():
    Q_sales = []
    q1 = input("Enter sales for Q1: ")
    q2 = input("Enter sales for Q2: ")
    q3 = input("Enter sales for Q3: ")
    q4 = input("Enter sales for Q4: ")
    Q_sales.append(q1)
    Q_sales.append(q2)
    Q_sales.append(q3)
    Q_sales.append(q4)

    return Q_sales, q1, q2, q3, q4

# solves for the quarter prices
def Q_prices(Q_sales, q1, q2, q3, q4):
    total = 0
    lowest = 0
    highest = 0
    count = len(Q_sales)
    total += float(q1)
    total += float(q2)
    total += float(q3)
    total += float(q4)
    total = round(total, 2)
    average = total / count
    average = round(average, 2)
    lowest = float(min(Q_sales))
    highest = float(max(Q_sales))
    lowest = round(lowest, 2)
    highest = round(highest, 2)

    return total, average, lowest, highest
# prints totals
def main():
    Q_sales, q1, q2, q3, q4 = get_sales()
    total, average, lowest, highest = Q_prices(Q_sales, q1, q2, q3, q4) 
    print("\ntotal:             ", total)
    print("average quarter:   ", average)
    print("lowest quarter:    ", lowest)
    print("highest quarter:   ", highest) 
main()
    
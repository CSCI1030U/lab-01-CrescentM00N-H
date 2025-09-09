def main():

# NAME: Hilaal Mansoor
# STUDENT ID: 100957010
# DATE: 2025-09-09


    # YOUR CODE FOR PART 1 GOES HERE  
    cost_per_item = 19.99
    quantity = 5 
    subtotal_cost = cost_per_item * quantity
    tax = subtotal_cost * 0.13
    total_cost = subtotal_cost + tax

# OUT PUT SHOULD BE:
# cost_per_item = $19.99
# quantity = 5
# subtotal_cost = $99.95
# tax = $12.99
# total_cost = $112.94


    # YOUR CODE FOR PART 2 GOES HERE
    print(f'cost_per_item = ${cost_per_item:0.2f}') # a sample for you to use for the other prices
    print(f'quantity = {quantity}')
    print(f'subtotal_cost = ${subtotal_cost:0.2f}')
    print(f'tax = ${tax:0.2f}')
    print(f'total_cost = ${total_cost:0.2f}')
    

    # THIS IS THE CODE FOR PART 3
    initial_investment = 1000
    interest_rate = 0.035
    investment = initial_investment
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    print('After 5 years, your investment will be worth ' + str(investment) + ' dollars.')
    # error: can only concatenate str (not "float") to str, so we need to convert investment to a string
    # expected output: After 5 years, your investment will be worth 1187.6863056468749 dollars.

if __name__ == "__main__":
    main()
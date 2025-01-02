 # CPGM120-01 SP24
# Matthew Mangus
# Mar. 17, 2024
# Assignment number 5
# Takes Vehicle and Trip Information and Calculates Required Output
# In-Line comments
# Updated last: Jan. 1, 2025

import sys


class Vehicle:
    Auto_Style = str()
    Make = str()
    Model = str()
    Color = str()
    Amount_Tank = float()
    Epa_Mpg = float()
    Actual_Mpg = float()
    Number_Wheels = int()
    Number_Doors = int()
    Total_Miles = float()
    Total_Length = float()


def gallons_used(total_miles: float, actual_mpg: float) -> float:
    """
    Function to obtain gallons used requiring
    total miles and actual mpg as input,
    gallons used is returned as output.
    """
    return float(total_miles / actual_mpg)


def fuel_required(total_miles: float, actual_mpg: float) -> float:
    """
    Function to obtain fuel required taking
    total miles and actual mpg as input,
    gallons of fuel is returned as output.
    :param total_miles:
    :param actual_mpg:
    :return:
    """
    return (total_miles / actual_mpg) / (total_miles * 100)


def tanks_consumed(total_miles: float, amount_tank: float) -> float:
    """
    Function to obtain tanks of fuel consumed taking
    total miles and amount of gallons per tank,
    returning tanks consumed as output.
    :param total_miles:
    :param amount_tank:
    :return:
    """
    return total_miles / amount_tank


def total_carbon(total_miles: float, actual_mpg: float) -> float:
    """
    Function to obtain total carbon emitted taking
    total miles and actual mpg as input,
    returning total carbon emitted as output.
    :param total_miles:
    :param actual_mpg:
    :return:
    """
    return (total_miles / actual_mpg) * 20


def main():
    """
    Main function to orchestrate program flow.
    :return:
    """
    try:
        while True:
            print('New Vehicle? Any Input for Yes or N/No:')
            new_vehicle = input()
            if (new_vehicle == 'N'
                    or new_vehicle == 'n'
                    or new_vehicle == 'No'
                    or new_vehicle == 'no'):
                sys.exit()
            else:
                Vehicle1 = Vehicle()
                print('Enter Automobile Style:')
                Vehicle1.Auto_Style = str(input())
                print('Enter Automobile Make:')
                Vehicle1.Make = str(input())
                print('Enter Automobile Model:')
                Vehicle1.Model = str(input())
                print('Enter Automobile Color:')
                Vehicle1.Color = str(input())
                print('Enter Automobile Gas Tank Capacity:')
                Vehicle1.Amount_Tank = float(input())
                print('Enter EPA MPG Estimation:')
                Vehicle1.Epa_Mpg = float(input())
                print('Enter Actual MPG:')
                Vehicle1.Actual_Mpg = float(input())
                print('Enter Number of Wheels:')
                Vehicle1.Number_Wheels = int(input())
                print('Enter Number of Doors:')
                Vehicle1.Number_Doors = int(input())
                print('Enter Total Miles Traveled:')
                Vehicle1.Total_Miles = float(input())
                print('Enter Total Length of Trip:')
                Vehicle1.Total_Length = float(input())

                # Perform Calculations for Output:
                var_gallons = gallons_used(
                    Vehicle1.Total_Miles, Vehicle1.Actual_Mpg)
                var_miles = fuel_required(
                    Vehicle1.Total_Miles, Vehicle1.Actual_Mpg)
                var_tanks = tanks_consumed(
                    Vehicle1.Total_Miles, Vehicle1.Amount_Tank)
                var_carbon = total_carbon(
                    Vehicle1.Total_Miles, Vehicle1.Actual_Mpg)

                print(f'{Vehicle1.Make} {Vehicle1.Model} '
                      f'has used {var_gallons} gallons of fuel')
                print(f'{Vehicle1.Make} {Vehicle1.Model} '
                      f'has {var_miles} miles left before fuel is needed')
                print(f'{Vehicle1.Make} {Vehicle1.Model} '
                      f'has consumed {var_tanks} tanks of fuel')
                print(f'{Vehicle1.Make} {Vehicle1.Model} '
                      f'has emitted {var_carbon} of carbon')

    except SyntaxError as err:
        print(f'Syntax Error has occurred: {err}')

    except TypeError as err:
        print(f'Type Error has occurred: {err}')


if __name__ == '__main__':
    main()

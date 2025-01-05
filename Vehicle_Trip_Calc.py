# CPGM120-01 SP24
# Matthew Mangus
# Mar. 17, 2024
# Assignment number 5
# Takes Vehicle and Trip Information and Calculates Required Output
# In-Line comments
# Updated last: Jan. 5, 2025

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
    Function to obtain gallons used by dividing total miles by actual mpg.

    Parameters:
        total_miles (float): Total miles of trip.
        actual_mpg (float): Actual miles per gallon.

    Returns:
        float: Gallons of fuel used.
    """
    return float(total_miles / actual_mpg)


def fuel_required(total_miles: float, actual_mpg: float) -> float:
    """
    Function to obtain fuel required by dividing total miles by actual mpg
    then dividing that by total miles multiplied by 100.

    Parameters:
        total_miles (float): Total miles of trip.
        actual_mpg (float): Actual miles per gallon.

    Returns:
        float: Gallons of fuel required.
    """
    return (total_miles / actual_mpg) / (total_miles * 100)


def tanks_consumed(total_miles: float, amount_tank: float) -> float:
    """
    Function to obtain tanks of fuel consumed obtained by dividing total miles
    by the gallon amount of tank.

    Parameters:
        total_miles (float): The total miles of trip.
        amount_tank (float): Amount of gallons per tank.

    Returns:
        float: Number of tanks consumed over trip.
    """
    return total_miles / amount_tank


def total_carbon(total_miles: float, actual_mpg: float) -> float:
    """
    Function to obtain total carbon emitted by dividing total miles by actual
    miles per gallon.

    Parameters:
        total_miles (float): Total miles travelled.
        actual_mpg (float): Actual miles per gallon.

    Returns:
        float: Amount of carbon produced.
    """
    return (total_miles / actual_mpg) * 20


def main() -> None:
    """
    Main function to orchestrate program flow and help with error handling.

    """
    try:
        while True:
            print('New Vehicle? Any Input for Yes or N/No:')
            new_vehicle:str = input()
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

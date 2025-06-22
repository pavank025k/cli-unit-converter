
"""
Temperature Conversion Tool

A command-line utility for converting between Celsius and Fahrenheit temperatures.
Uses argparse for robust command-line argument handling and provides clear output.
"""

import argparse


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius: Temperature in degrees Celsius
        
    Returns:
        Temperature in degrees Fahrenheit
    """
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert temperature from Fahrenheit to Celsius.
    
    Args:
        fahrenheit: Temperature in degrees Fahrenheit
        
    Returns:
        Temperature in degrees Celsius
    """
    return (fahrenheit - 32) * 5/9


def parse_arguments():
    """Configure and parse command-line arguments.
    
    Returns:
        Namespace object containing parsed arguments
    """
    parser = argparse.ArgumentParser(
        prog="temp_converter",
        description="Convert temperatures between Celsius and Fahrenheit",
        epilog="Example: temp_converter -c 25 (converts 25°C to Fahrenheit)"
    )
    
    # Mutually exclusive group ensures only one conversion type is specified
    conversion_group = parser.add_mutually_exclusive_group(required=True)
    conversion_group.add_argument(
        "-c", "--celsius",
        type=float,
        metavar="TEMPERATURE",
        help="temperature in Celsius to convert to Fahrenheit"
    )
    conversion_group.add_argument(
        "-f", "--fahrenheit",
        type=float,
        metavar="TEMPERATURE",
        help="temperature in Fahrenheit to convert to Celsius"
    )
    
    # Optional argument for output precision
    parser.add_argument(
        "-p", "--precision",
        type=int,
        default=2,
        choices=range(0, 6),
        metavar="DIGITS",
        help="number of decimal places in output (0-5, default: 2)"
    )
    
    return parser.parse_args()


def format_output(original: float, converted: float, unit_from: str, unit_to: str, precision: int) -> str:
    """Format the conversion result for clean output.
    
    Args:
        original: Original temperature value
        converted: Converted temperature value
        unit_from: Original temperature unit ('C' or 'F')
        unit_to: Converted temperature unit ('F' or 'C')
        precision: Number of decimal places to display
        
    Returns:
        Formatted output string
    """
    return f"{original:.{precision}f}°{unit_from} = {converted:.{precision}f}°{unit_to}"


def main():
    """Main program execution."""
    try:
        args = parse_arguments()
        
        if args.celsius is not None:
            converted_temp = celsius_to_fahrenheit(args.celsius)
            output = format_output(
                args.celsius, converted_temp, 'C', 'F', args.precision
            )
        else:
            converted_temp = fahrenheit_to_celsius(args.fahrenheit)
            output = format_output(
                args.fahrenheit, converted_temp, 'F', 'C', args.precision
            )
            
        print(output)
        
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        exit(0)


if __name__ == "__main__":
    main()
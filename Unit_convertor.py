def convert_units(category, from_unit, to_unit, value):
    if category == "Length":
        conversion = {
            "Meters": 1,
            "Kilometers": 1000,
            "Miles": 1609.34,
            "Feet": 0.3048,
            "Inches": 0.0254
        }
        return value * conversion[from_unit] / conversion[to_unit]
    
    elif category == "Weight":
        conversion = {
            "Grams": 1,
            "Kilograms": 1000,
            "Pounds": 453.592,
            "Ounces": 28.3495
        }
        return value * conversion[from_unit] / conversion[to_unit]
    
    elif category == "Temperature":
        if from_unit == to_unit:
            return value
        elif from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return value * 9/5 + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32

def main():
    print("🔁 Google-style Unit Converter")
    categories = {
        "1": "Length",
        "2": "Weight",
        "3": "Temperature"
    }

    print("\nSelect a category:")
    for key, value in categories.items():
        print(f"{key}. {value}")
    
    choice = input("Enter choice (1/2/3): ")
    category = categories.get(choice)

    if not category:
        print("❌ Invalid category.")
        return

    units = {
        "Length": ["Meters", "Kilometers", "Miles", "Feet", "Inches"],
        "Weight": ["Grams", "Kilograms", "Pounds", "Ounces"],
        "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
    }

    print("\nAvailable units:")
    for idx, unit in enumerate(units[category]):
        print(f"{idx + 1}. {unit}")

    try:
        from_unit = units[category][int(input("Convert from (number): ")) - 1]
        to_unit = units[category][int(input("Convert to (number): ")) - 1]
        value = float(input("Enter value to convert: "))
        result = convert_units(category, from_unit, to_unit, value)
        print(f"\n✅ {value} {from_unit} = {result:.4f} {to_unit}")
    except (IndexError, ValueError):
        print("❌ Invalid input. Please try again.")

if __name__ == "__main__":
    main()

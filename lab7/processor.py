def parse_transit_corridor(corridor_code):
    """
    Parse a transit corridor code of the form ORIG-DEST-ZONES.
    Returns a formatted route string, or a safe error message on invalid input.
    """
    try:
        if corridor_code is None:
            return "Error: corridor code cannot be None"
        if not isinstance(corridor_code, str):
            return f"Error: expected string, got {type(corridor_code).__name__}"

        cleaned = corridor_code.strip()
        if not cleaned:
            return "Error: empty corridor code"

        parts = cleaned.split('-')
        if len(parts) != 3:
            return "Error: corridor code must be in format ORIG-DEST-ZONES"

        orig, dest, zones_str = parts
        if not orig or not dest:
            return "Error: origin and destination cannot be empty"

        try:
            zones = int(zones_str)
        except ValueError:
            return f"Error: zones must be an integer, got '{zones_str}'"

        if zones < 0:
            return "Error: number of zones cannot be negative"

        base_fare = 2.50 + (zones * 0.75)
        return f"Route {orig.upper()}->{dest.upper()}: {zones} Zones, Fare ${base_fare:.2f}"
    except Exception as e:
        return f"Error: unexpected failure while parsing corridor ({type(e).__name__}: {e})"


def lookup_concession_discount(category_name):
    """
    Look up the fare multiplier for a concession category.
    Returns the multiplier (float) or a safe default / error message on invalid input.
    """
    try:
        if category_name is None:
            return "Error: category name cannot be None"
        if not isinstance(category_name, str):
            return f"Error: expected string, got {type(category_name).__name__}"

        category = category_name.strip().upper()
        if not category:
            return "Error: empty category name"

        discounts = {
            "STANDARD": 1.00,
            "STUDENT": 0.50,
            "SENIOR": 0.35,
            "MILITARY": 0.20,
            "CHILD": 0.00,
        }
        if category not in discounts:
            return f"Error: unknown concession category '{category_name.strip()}'"

        return discounts[category]
    except Exception as e:
        return f"Error: unexpected failure while looking up concession ({type(e).__name__}: {e})"


def compute_passenger_density(occupancy_ratio_str):
    """
    Compute passengers per km from a string of the form 'passengers/km'.
    Returns the rounded density (float) or a safe error message on invalid input.
    """
    try:
        if occupancy_ratio_str is None:
            return "Error: occupancy ratio cannot be None"
        if not isinstance(occupancy_ratio_str, str):
            return f"Error: expected string, got {type(occupancy_ratio_str).__name__}"

        cleaned = occupancy_ratio_str.strip()
        if not cleaned:
            return "Error: empty occupancy ratio"

        parts = cleaned.split('/')
        if len(parts) != 2:
            return "Error: occupancy ratio must be in format passengers/km"

        passengers_str, km_str = parts
        try:
            passengers = float(passengers_str)
            km = float(km_str)
        except ValueError:
            return "Error: passengers and km must be numeric values"

        if km == 0:
            return "Error: kilometres cannot be zero (division by zero)"

        if passengers < 0 or km < 0:
            return "Error: passengers and kilometres cannot be negative"

        density = passengers / km
        return round(density, 2)
    except Exception as e:
        return f"Error: unexpected failure while computing density ({type(e).__name__}: {e})"


def main():
    print("==== Running parse_transit_corridor ====")
    c_input = input("Enter corridor (e.g. DT-UP-3): ")
    print(parse_transit_corridor(c_input))

    print("\n==== Running lookup_concession_discount ====")
    cat_input = input("Enter concession category (e.g. STUDENT, SENIOR): ")
    print("Multiplier:", lookup_concession_discount(cat_input))

    print("\n==== Running compute_passenger_density ====")
    d_input = input("Enter passengers/km (e.g. 50/10.0): ")
    print("Density:", compute_passenger_density(d_input))


if __name__ == "__main__":
    main()

import math


def parse_transit_corridor(corridor_code):
    if not isinstance(corridor_code, str):
        return "Invalid corridor: input must be text"
    parts = corridor_code.strip().split('-')
    if len(parts) != 3:
        return "Invalid corridor: expected format ORIGIN-DEST-ZONES"
    orig, dest, zones_str = parts
    if not orig.strip() or not dest.strip():
        return "Invalid corridor: origin and destination cannot be empty"
    try:
        zones = int(zones_str)
    except (ValueError, OverflowError):
        return "Invalid corridor: zones must be a whole number"
    if zones < 0 or zones > 1000:
        return "Invalid corridor: zones out of range"
    base_fare = 2.50 + (zones * 0.75)
    return f"Route {orig.upper()}->{dest.upper()}: {zones} Zones, Fare ${base_fare:.2f}"


def lookup_concession_discount(category_name):
    if not isinstance(category_name, str):
        return None
    category = category_name.strip().upper()
    discounts = {
        "STANDARD": 1.00,
        "STUDENT": 0.50,
        "SENIOR": 0.35,
        "MILITARY": 0.20,
        "CHILD": 0.00
    }
    return discounts.get(category)


def compute_passenger_density(occupancy_ratio_str):
    if not isinstance(occupancy_ratio_str, str):
        return None
    parts = occupancy_ratio_str.split('/')
    if len(parts) != 2:
        return None
    try:
        passengers = float(parts[0])
        km = float(parts[1])
        density = passengers / km
    except (ValueError, ZeroDivisionError, OverflowError):
        return None
    if math.isnan(density) or math.isinf(density):
        return None
    return round(density, 2)


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
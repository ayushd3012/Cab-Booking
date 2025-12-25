import json
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class CabService:
    def __init__(self, filename="bookings.json"):
        self.filename = filename
        self.fares = {
            "Uber Bike": 5,   # 	5 per km
            "Uber Auto": 8,   # 	8 per km
            "Uber Cab": 11,    # 	11 per km
            "Uber XL": 14      # 	14 per km
        }
        # average speeds in km/h for estimated journey time
        self.speeds = {
            "Uber Bike": 30,
            "Uber Auto": 45,
            "Uber Cab": 65,
            "Uber XL": 75
        }
        self.history = self.load_history()

    def available_options(self, people):
        if people == 1:
            return ["Uber Bike", "Uber Auto", "Uber Cab"]
        elif 2 <= people <= 3:
            return ["Uber Auto", "Uber Cab"]
        elif people == 4:
            return ["Uber Cab"]
        elif 5 <= people <= 7:
            return ["Uber XL"]
        else:
            return []

    def book_cab(self, people, cab_type, distance):
        options = self.available_options(people)
        if cab_type not in options:
            return f"❌ {cab_type} not available for {people} people."

        try:
            distance = float(distance)
        except Exception:
            return "❌ Invalid distance. Please enter a number."
        if distance <= 0:
            return "❌ Distance must be positive."

        fare = self.fares[cab_type] * distance
        speed = self.speeds.get(cab_type, None)
        est_str = "N/A"
        if speed and speed > 0:
            hours = distance / speed
            total_seconds = int(hours * 3600)
            h, rem = divmod(total_seconds, 3600)
            m, s = divmod(rem, 60)
            est_str = f"{h}h {m}m {s}s"

        booking = {
            "people": people,
            "cab_type": cab_type,
            "distance": distance,
            "fare": round(fare, 2),
            "estimated_time": est_str
        }
        self.history.append(booking)
        self.save_history()
        return f"✅ Booking confirmed: {cab_type} for {people} people, Distance: {distance} km, Fare: ₹{round(fare,2)}, Est. time: {est_str}"

    def save_history(self):
        with open(self.filename, "w") as f:
            json.dump(self.history, f, indent=4)

    def load_history(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return []

    def show_history(self):
        if not self.history:
            return "No bookings yet."
        result = "\n--- Booking History ---\n"
        for i, b in enumerate(self.history, 1):
            est = b.get('estimated_time', 'N/A')
            result += f"{i}. {b['cab_type']} | People: {b['people']} | Distance: {b['distance']} km | Fare: ₹{b['fare']} | Est. time: {est}\n"
        return result


# Example usage
service = CabService()

# First-run initialization (default): create padding.txt with 100 blank lines.
init_marker = ".cab_booking_initialized"
padding_file = "padding.txt"
if not os.path.exists(init_marker):
    with open(padding_file, "a", encoding="utf-8") as f:
        f.write("\n" * 100)
    with open(init_marker, "w", encoding="utf-8") as f:
        f.write("initialized")
    print(f"Initialization: created '{padding_file}' with 100 blank lines.")

# Clear the terminal screen on program start
clear_screen()

while True:
    try:
        people = int(input("Enter number of people travelling: "))
    except ValueError:
        print("❌ Invalid input. Please enter an integer for number of people.")
        continue

    options = service.available_options(people)
    
    if not options:
        print("❌ No suitable cab available.")
    else:
        if len(options) == 1:
            cab_type = options[0]
            print(f"Only available option is '{cab_type}'. Selecting it by default.")
        else:
            print("Available options:", ", ".join(options))
            # accept case-insensitive input and trim whitespace; re-prompt until valid
            while True:
                cab_input = input("Choose ride type: ").strip()
                matched = next((opt for opt in options if opt.lower() == cab_input.lower()), None)
                if matched:
                    cab_type = matched
                    break
                else:
                    print("❌ Invalid option. Please choose one of:", ", ".join(options))
        distance = input("Enter distance (in km): ").strip()
        print(service.book_cab(people, cab_type, distance))
    
    more = input("Do you want to book another ride? (yes/no): ").lower()
    if more != "yes":
        break

print(service.show_history())
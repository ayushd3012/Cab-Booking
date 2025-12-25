# Cab Booking — Quick Start (Standalone)

A lightweight command-line cab booking helper that suggests ride options based on party size, accepts case-insensitive ride choices, validates input, and stores booking history.

## Highlights ✅
- Case-insensitive ride selection (trimmed input accepted)
- Auto-selects the only available ride option when applicable
- Validates numeric inputs (people & distance)
- Saves bookings to `bookings.json` and prints a summary at exit
- First-run setup: creates `padding.txt` with blank lines and a `.cab_booking_initialized` marker
- Clears the terminal screen at startup (cross-platform)

## Quick Usage
1. Open a terminal in the `Python` folder.
2. Run the script:
   - Windows: `python "Cab Booking.py"`
   - POSIX: `python3 "Cab Booking.py"`
3. Follow prompts:
   - Number of people (integer)
   - Ride type (case-insensitive; auto-selected if only 1 option)
   - Distance in km

Example session:
```
Enter number of people travelling: 4
Only available option is 'Uber Cab'. Selecting it by default.
Enter distance (in km): 10
✅ Booking confirmed: Uber Cab for 4 people, Distance: 10.0 km, Fare: ₹110.0, Est. time: 0h 9m 13s
```

## Files produced/used
- `bookings.json` — booking history
- `padding.txt` — created on first run (contains blank lines)
- `.cab_booking_initialized` — marker file to prevent repeating first-run steps

## Customization
- Edit `Cab Booking.py` to change number of padding lines or to disable first-run behavior.
- The helper function `clear_screen()` (near top of file) is used to clear the terminal on startup.

---

If you'd like small edits to the wording or an expanded example (e.g., show history contents), tell me and I'll update this file accordingly.
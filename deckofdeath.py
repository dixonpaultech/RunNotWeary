import random
from copy import deepcopy
import time


# ==========================================================
# BUILD DECKS
# Each card = (exercise_name, duration_seconds)
# ==========================================================

upper_body_deck = [
    ("Push-ups", 3),    
    ("Push-ups", 4),
    ("Push-ups", 5),
    ("Push-ups", 7),

    ("Diamond Push-ups", 3),    
    ("Diamond Push-ups", 4),
    ("Diamond Push-ups", 5),
    ("Diamond Push-ups", 7),

    ("Wide Push-ups", 3),    
    ("Wide Push-ups", 4),
    ("Wide Push-ups", 5),
    ("Wide Push-ups", 7),

    ("Pike Push-ups", 3),    
    ("Pike Push-ups", 4),
    ("Pike Push-ups", 5),
    ("Pike Push-ups", 7),

    ("Incline Push-ups", 3),    
    ("Incline Push-ups", 4),
    ("Incline Push-ups", 5),
    ("Incline Push-ups", 7),

    ("Decline Push-ups", 3),    
    ("Decline Push-ups", 4),
    ("Decline Push-ups", 5),
    ("Decline Push-ups", 7),

    ("Chair Dips", 3),    
    ("Chair Dips", 4),
    ("Chair Dips", 5),
    ("Chair Dips", 7),

    ("Slow Push-ups", 3),    
    ("Slow Push-ups", 4),
    ("Slow Push-ups", 5),
    ("Slow Push-ups", 7),

    ("Explosive Push-ups", 3),    
    ("Explosive Push-ups", 4),
    ("Explosive Push-ups", 5),
    ("Explosive Push-ups", 7),

    ("Shoulder Taps", 3),    
    ("Shoulder Taps", 4),
    ("Shoulder Taps", 5),
    ("Shoulder Taps", 7),

    ("Plank Up-Downs", 3),    
    ("Plank Up-Downs", 4),
    ("Plank Up-Downs", 5),
    ("Plank Up-Downs", 7),

    ("Wall Push-ups", 7),    
    ("Wall Push-ups", 10),
    ("Wall Push-ups", 12),
    ("Wall Push-ups", 15),

    ("Archer Push-ups", 3),    
    ("Archer Push-ups", 4),
    ("Archer Push-ups", 5),
    ("Archer Push-ups", 7),

]

upper_body_deck = upper_body_deck[:52]


lower_body_deck = [
    ("Bodyweight Squats", 3),           
    ("Bodyweight Squats", 4),        
    ("Bodyweight Squats", 5),          
    ("Bodyweight Squats", 7),          
  
    ("Jump Squats", 3),    
    ("Jump Squats", 4),
    ("Jump Squats", 5),
    ("Jump Squats", 7),

    ("Reverse Lunges", 3),    
    ("Reverse Lunges", 4),
    ("Reverse Lunges", 5),
    ("Reverse Lunges", 7),

    ("Walking Lunges", 3),    
    ("Walking Lunges", 4),
    ("Walking Lunges", 5),
    ("Walking Lunges", 7),

    ("Split Squats", 3),    
    ("Split Squats", 4),
    ("Split Squats", 5),
    ("Split Squats", 7),

    ("Wall Sit", 10),    
    ("Wall Sit", 12),
    ("Wall Sit", 15),
    ("Wall Sit", 20),

    ("Calf Raises", 10),    
    ("Calf Raises", 12),
    ("Calf Raises", 15),
    ("Calf Raises", 20),

    ("Single-Leg Glute Bridge", 3),    
    ("Single-Leg Glute Bridge", 4),
    ("Single-Leg Glute Bridge", 5),
    ("Single-Leg Glute Bridge", 7),

    ("Glute Bridge", 7 ),   
    ("Glute Bridge", 10),
    ("Glute Bridge", 12),
    ("Glute Bridge", 15),

    ("Squat Pulses", 7 ),    
    ("Squat Pulses", 10),
    ("Squat Pulses", 12),
    ("Squat Pulses", 15),

    ("Step-Ups", 7 ),   
    ("Step-Ups", 10),
    ("Step-Ups", 12),
    ("Step-Ups", 15),

    ("Lateral Lunges", 3),   
    ("Lateral Lunges", 4),
    ("Lateral Lunges", 5),
    ("Lateral Lunges", 7),

    ("Broad Jumps", 3),    
    ("Broad Jumps", 4),
    ("Broad Jumps", 5),
    ("Broad Jumps", 7),

]

lower_body_deck = lower_body_deck[:52]


core_cardio_deck = [
    ("Plank", 10),      
    ("Plank", 12),  
    ("Plank", 15),  
    ("Plank", 20),  

    ("Side Plank Left", 10),    
    ("Side Plank Left", 12),
    ("Side Plank Left", 15),
    ("Side Plank Left", 20),

    ("Side Plank Right", 10),    
    ("Side Plank Right", 12),
    ("Side Plank Right", 15),
    ("Side Plank Right", 20),

    ("High Knees", 10),    
    ("High Knees", 12),
    ("High Knees", 15),
    ("High Knees", 20),

    ("Burpees", 3),    
    ("Burpees", 4),
    ("Burpees", 5),
    ("Burpees", 7),

    ("Russian Twists", 7 ),    
    ("Russian Twists", 10),
    ("Russian Twists", 12),
    ("Russian Twists", 15),

    ("Leg Raises", 7 ),    
    ("Leg Raises", 10),
    ("Leg Raises", 12),
    ("Leg Raises", 15),

    ("Flutter Kicks", 7 ),    
    ("Flutter Kicks", 10),
    ("Flutter Kicks", 12),
    ("Flutter Kicks", 15),

    ("Bicycle Crunches", 10),    
    ("Bicycle Crunches", 12),
    ("Bicycle Crunches", 15),
    ("Bicycle Crunches", 20),

    ("Jumping Jacks", 10),    
    ("Jumping Jacks", 12),
    ("Jumping Jacks", 15),
    ("Jumping Jacks", 20),

    ("Bear Crawl Hold", 7 ),    
    ("Bear Crawl Hold", 10),
    ("Bear Crawl Hold", 12),
    ("Bear Crawl Hold", 15),

    ("V-Ups", 3),    
    ("V-Ups", 4),
    ("V-Ups", 5),
    ("V-Ups", 7),

    ("Mountain Climbers", 7 ),    
    ("Mountain Climbers", 10),
    ("Mountain Climbers", 12),
    ("Mountain Climbers", 15),

]

core_cardio_deck = core_cardio_deck[:52]


# ==========================================================
# DECK SELECTION
# ==========================================================

decks = {
    "1": ("Upper Body", upper_body_deck),
    "2": ("Lower Body", lower_body_deck),
    "3": ("Core & Cardio", core_cardio_deck)
}

print("Workout Card Decks")
print("------------------")
print("1. Upper Body")
print("2. Lower Body")
print("3. Core & Cardio")

choice = input("\nChoose a deck (1-3): ").strip()

while choice not in decks:
    choice = input("Please enter 1, 2, or 3: ").strip()

deck_name, original_deck = decks[choice]

# Make a copy so the original stays unchanged
shuffled_deck = deepcopy(original_deck)
random.shuffle(shuffled_deck)
random.shuffle(shuffled_deck)
random.shuffle(shuffled_deck)

print(f"\nSelected Deck: {deck_name}")
print("Complete the exercise before drawing the next card.\n")
start_time = time.time()

# ==========================================================
# DRAW CARDS
# ==========================================================

total_seconds = 0

for card_number, (exercise, duration) in enumerate(shuffled_deck, start=1):

    input(f"Card {card_number}/52 - Press ENTER to draw...")

    print("\n===================================")
    print(f"Exercise: {duration} {exercise}")
    print("===================================\n")

    total_seconds += duration

input(f"Finished? - Press ENTER to draw...")
# ==========================================================
# SUMMARY
# ==========================================================

end_time = time.time()
elapsed = end_time - start_time

minutes = int(elapsed // 60)
seconds = int(elapsed % 60)

print("\nDeck Complete!")
print("---------------------------")
print(f"Total Exercise Time: {minutes} minutes {seconds} seconds")
print("---------------------------")
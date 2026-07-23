print("Duplicate Attendee List\n")
# Student list with a duplicate attendee
attendees = ["Anand", "Akbar", "Chvhan", "Chavhan", "Dhoni"]
print("Original list:", attendees)
print("\n")


# Remove the duplicate entry
removed_name=attendees.remove("Chavhan")
print("After removing duplicate:", attendees)
print("Removed name:", removed_name)

# Archive at year-end by resetting the list
attendees.clear()
print("After archiving (cleared):", attendees)
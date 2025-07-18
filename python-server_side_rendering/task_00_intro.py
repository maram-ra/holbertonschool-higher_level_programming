import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for idx, attendee in enumerate(attendees, start=1):
        filled_template = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key) or "N/A"
            filled_template = filled_template.replace(f"{{{key}}}", str(value))
        
        file_name = f"output_{idx}.txt"
        with open(file_name, "w") as f:
            f.write(filled_template)

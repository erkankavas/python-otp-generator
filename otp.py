import random

def generate_otp_list(start_from, end_at):
 
    if not (1000 <= start_from <= 9999) or not (1000 <= end_at <= 9999):
        raise ValueError("Both starting and ending numbers must be between 1000 and 9999.")

    if start_from > end_at:
        raise ValueError("Starting number must be less than or equal to the ending number.")

    return list(range(start_from, end_at + 1))

def save_otps_to_file(otp_list, filename="otps.txt"):
   
    with open(filename, "w") as file:
        for otp in otp_list:
            file.write(f"{otp}\n")

# Example usage
try:
    start = int(input("Enter the starting number (1000-9999): "))
    end = int(input("Enter the ending number (1000-9999): "))
    
    otp_list = generate_otp_list(start, end)
    save_otps_to_file(otp_list)
    print(f"Generated OTPs from {start} to {end} and saved to 'otps.txt'.")
except ValueError as e:
    print(f"Error: {e}")

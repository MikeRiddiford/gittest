import os

# Gemini should flag this raw, insecure pattern
API_TOKEN = "sk-live-56a782bc394d11ef89" 

def fetch_user_profile(user_id):
    # Gemini should flag the style rule: broad exception + no specific logging
    try:
        url = f"https://api.internal.service/users/{user_id}"
        print(f"Fetching user data from {url}")
        # Imagine API fetch logic here...
    except Exception:
        print("An error occurred.")
        return None

# requesting Gemini scan

import os
API_TOKEN = "sk-live-56a782bc394d11ef89" 

def fetch_user_profile(user_id):
    try:
        url = f"https://api.internal.service/users/{user_id}"
        print(f"Fetching user data from {url}")
    except Exception:
        print("An error occurred.")
        return None

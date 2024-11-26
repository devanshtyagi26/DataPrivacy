import hashlib
import requests

def check_password_leak(password):
    # Hash the password using SHA-1
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    # Split the hash into the first 5 characters (prefix) and the rest (suffix)
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    # Query the Have I Been Pwned API
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(f"Error fetching data from Have I Been Pwned API: {response.status_code}")

    # Check if the suffix appears in the API response
    hashes = response.text.splitlines()
    for hash_entry in hashes:
        hash_suffix, count = hash_entry.split(":")
        if suffix == hash_suffix:
            return int(count)

    # If no match is found, return 0
    return 0


def process_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        print(f"{'Username':<20}{'Password':<20}{'Leak Count':<10}")
        print("=" * 50)

        for line in lines:
            # Parse each line (assume format is "username,password")
            username, password = line.strip().split(",")

            # Check if the password has been leaked
            leak_count = check_password_leak(password)

            # Display the results
            print(f"{username:<20}{password:<20}{leak_count:<10}")

            if leak_count > 0:
                print(f"WARNING: Password for {username} has been leaked {leak_count} times!\n")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


    # Input: File containing usernames and passwords
filename = input("Enter the filename (e.g., 'users.txt'): ")
process_file(filename)

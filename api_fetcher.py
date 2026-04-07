import requests

def fetch_users():
    try:
        url = "https://jsonplaceholder.typicode.com/users"
        response = requests.get(url)
        response.raise_for_status()  # error handling

        data = response.json()  # JSON parsing
        return data

    except requests.exceptions.RequestException as e:
        print("❌ Error fetching data:", e)
        return []


def search_user(users, keyword):
    results = []
    for user in users:
        if keyword.lower() in user['name'].lower():
            results.append(user)
    return results


def display_users(users):
    if not users:
        print("⚠️ No users found.")
        return

    print("\n📋 User Data:\n")
    for user in users:
        print(f"Name   : {user['name']}")
        print(f"Email  : {user['email']}")
        print(f"City   : {user['address']['city']}")
        print("-" * 30)


def main():
    users = fetch_users()

    while True:
        print("\n🔍 MENU")
        print("1. Show all users")
        print("2. Search user")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            display_users(users)

        elif choice == '2':
            keyword = input("Enter name to search: ")
            filtered = search_user(users, keyword)
            display_users(filtered)

        elif choice == '3':
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
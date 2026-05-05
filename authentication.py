user_database = {
    "admin": ("password123", "admin", True, "System Admin", False, "admin@example.com", True, True, set(), [], 0, 0),
}

active_usernames = set(username for username, (_, _, active, _, _, _, _, _, _, _, _, _) in user_database.items() if active)
logged_in_users = set()
admin_notifications = []
verification_codes = {}


def is_strong_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_underscore = False
    has_special = False
    
    for char in password:
        if char >= 'A' and char <= 'Z':
            has_upper = True
        if char >= 'a' and char <= 'z':
            has_lower = True
        if char >= '0' and char <= '9':
            has_digit = True
        if char == '_':
            has_underscore = True
        if char in ('!', '@', '#', '$', '%'):
            has_special = True
    
    is_long = len(password) >= 8
    
    if not is_long:
        return False, "Password must be at least 8 characters long."
    if not has_upper:
        return False, "Password must contain at least one uppercase letter."
    if not has_lower:
        return False, "Password must contain at least one lowercase letter."
    if not has_digit:
        return False, "Password must contain at least one number."
    if not has_underscore:
        return False, "Password must contain at least one underscore (_)."
    if not has_special:
        return False, "Password must contain at least one special character (! @ # $ %)."
    
    return True, "Password is strong!"


def is_valid_email(email):
    if "@" not in email:
        return False
    if not email.endswith("@email.com"):
        return False
    if email.count("@") != 1:
        return False
    return True


def is_valid_username(username):
    if not username:
        return False, "Username cannot be empty."
    if "_" not in username:
        return False, "Username must contain at least one underscore (_)."
    for char in username:
        if char not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-":
            return False, "Enter a valid username!"
    return True, "Valid username."


def generate_verification_code():
    import random
    return ''.join(str(random.randint(0, 9)) for _ in range(6))


def send_email_code(username, purpose):
    if username not in user_database:
        return
    password, role, active, display_name, hacked_reported, email, email_verified, two_factor_enabled, friends, posts, followers, likes = user_database[username]
    code = generate_verification_code()
    verification_codes[username] = (code, purpose)
    print(f"\n[Email sent to {email}] {purpose} verification code: {code}\n")


def authenticate(username, password):
    if username not in active_usernames:
        return False, None, "Invalid credentials."
    user_data = user_database[username]
    if user_data[4]:  
        return False, None, """
***********************************************
*                                             *
*               ACCOUNT HACKED!               *
*                                             *
*  Your account has been compromised.         *
*  Please contact admin for recovery.         *
*                                             *
***********************************************
"""
    if user_data[0] == password:
        return True, user_data[1], None
    else:
        return False, None, "Invalid credentials."


def send_hack_alert(username):
    if username not in user_database:
        print("Unknown account. Cannot send notification.")
        return
    password, role, active, display_name, hacked_reported, email, email_verified, two_factor_enabled, friends, posts, followers, likes = user_database[username]
    if hacked_reported:
        print("Admin already received a hack report for this account.")
        return
    user_database[username] = (password, role, active, display_name, True, email, email_verified, two_factor_enabled, friends, posts, followers, likes)
    admin_notifications.append((username, display_name))
    print("Admin has been notified: your account has been reported as hacked.")


def register():
    print("=======================================")
    print("         -| Registration |-")
    print("======================================")
    print("\n-------------------------------------")
    print("      -| Password Requirements: |-")
    print("---------------------------------------")
    print("- | At least 8 characters             |")
    print("- | One uppercase letter              |")
    print("- | One lowercase letter              |")
    print("- | One number                        |")
    print("- | One underscore (_)                |")
    print("- | One special character (! @ # $ %) |")
    print("")
    
    while True:
        username = input("| Enter new username |: ")
        if username in user_database:
            print("Username already exists. Please choose a different one.")
            continue
        is_valid, message = is_valid_username(username)
        if not is_valid:
            print(f"Invalid username: {message}")
            continue
        break
    
    display_name = input("| Enter display name |: ")
    
    while True:
        email = input("| Enter email address |: ")
        if not is_valid_email(email):
            print("Invalid email address. Must use the format username@email.com.")
            continue
        break
    
    while True:
        password = input("| Enter password |: ")
        is_strong, message = is_strong_password(password)
        if is_strong:
            break
        else:
            print(f"Weak password: {message}")
    
    while True:
        confirm_password = input("| Confirm password |: ")
        if password != confirm_password:
            print("Passwords do not match. Please try again.")
            continue
        break
    
    user_database[username] = (password, "user", True, display_name, False, email, False, True, set(), [], 0, 0)
    active_usernames.add(username)
    send_email_code(username, "Email verification")
    print("Registration successful! A verification code has been sent to your email.")
    verify_email_address(username)


def verify_email_address(username):
    if username not in user_database:
        return
    _, role, _, display_name, _, email, email_verified, _, _, _, _, _ = user_database[username]
    if email_verified:
        print("Email already verified.")
        return
    print("\nEmail verification required.")
    for _ in range(3):
        code = input("| Enter the verification code sent to your email |: ")
        if username in verification_codes and verification_codes[username][0] == code:
            password, role, active, display_name, hacked_reported, email, _, two_factor_enabled, friends, posts, followers, likes = user_database[username]
            user_database[username] = (password, role, active, display_name, hacked_reported, email, True, two_factor_enabled, friends, posts, followers, likes)
            del verification_codes[username]
            print("Email verified successfully.")
            return
        else:
            print("Invalid code. Try again.")
    print("Email verification failed. Please request a new verification code.")


def require_two_factor(username):
    if username not in user_database:
        return False
    password, role, active, display_name, hacked_reported, email, email_verified, two_factor_enabled, friends, posts, followers, likes = user_database[username]
    if not email_verified:
        print("Email not verified. Please verify your email first.")
        verify_email_address(username)
        return False
    if not two_factor_enabled:
        return True
    send_email_code(username, "2-step verification")
    for _ in range(3):
        code = input("| Enter the 2-step verification code sent to your email |: ")
        if username in verification_codes and verification_codes[username][0] == code:
            del verification_codes[username]
            print("2-step verification passed.")
            return True
        else:
            print("Invalid code. Try again.")
    print("2-step verification failed.")
    return False


def login():
    print("====================")
    print("     -| Login |-    ")
    print("====================")
    username = input("| Enter username |: ")
    password = input("| Enter password |: ")

    success, role, message = authenticate(username, password)
    if success:
        if not require_two_factor(username):
            return None, None
        logged_in_users.add(username)
        display_name = user_database[username][3]
        print("Authentication successful!")
        print(f"Welcome, {display_name}! You are logged in as {role}.")
        return username, role
    else:
        print(message)
        return None, None


def logout(username):
    if username in logged_in_users:
        logged_in_users.remove(username)
        print(f"{username} logged out successfully.")
    else:
        print("No user logged in.")


def display_menu(role):
    if role == "admin":
        print("====================")
        print("  -|Admin Menu:  |-")
        print("====================")
        print("1. View all users")
        print("2. View logged in users")
        print("3. View hack reports")
        print("4. Recover hacked account")
        print("5. Logout")
        print("6. Return to main menu")
    else:
        print("====================")
        print("   -|User Menu:  |- ")
        print("====================")
        print("1. View profile")
        print("2. Account management")
        print("3. Email management")
        print("4. Social networking")
        print("5. Report hacked account")
        print("6. Logout")
        print("7. Return to main menu")


def account_management(username):
    while True:
        print("\nAccount Management:")
        print("1. Change username")
        print("2. Change display name")
        print("3. Change password")
        print("4. Update email address")
        print("5. Toggle 2-step verification")
        print("6. Back")
        choice = input("| Enter your choice |: ")
        match choice:
            case "1":
                while True:
                    new_username = input("| Enter new username |: ")
                    if new_username in user_database:
                        print("Username already exists. Choose another.")
                        continue
                    is_valid, message = is_valid_username(new_username)
                    if not is_valid:
                        print(f"Invalid username: {message}")
                        continue
                    break
                password, role, active, display_name, hacked_reported, email, email_verified, two_factor_enabled, friends, posts, followers, likes = user_database.pop(username)
                user_database[new_username] = (password, role, active, display_name, hacked_reported, email, email_verified, two_factor_enabled, friends, posts, followers, likes)
                if username in active_usernames:
                    active_usernames.remove(username)
                    active_usernames.add(new_username)
                if username in logged_in_users:
                    logged_in_users.remove(username)
                    logged_in_users.add(new_username)
                print("Username updated successfully.")
                return new_username
            case "2":
                password, role, active, display_name, hacked_reported, email, email_verified, two_factor_enabled, friends, posts, followers, likes = user_database[username]
                new_display = input("| Enter new display name |: ")
                user_database[username] = (password, role, active, new_display, hacked_reported, email, email_verified, two_factor_enabled, friends, posts, followers, likes)
                print("Display name updated successfully.")
            case "3":
                while True:
                    new_password = input("| Enter new password |: ")
                    is_strong, message = is_strong_password(new_password)
                    if is_strong:
                        break
                    else:
                        print(f"Weak password: {message}")
                while True:
                    confirm_password = input("| Confirm new password |: ")
                    if new_password != confirm_password:
                        print("Passwords do not match. Please try again.")
                        continue
                    break
                password, role, active, display_name, hacked_reported, email, email_verified, two_factor_enabled, friends, posts, followers, likes = user_database[username]
                user_database[username] = (new_password, role, active, display_name, hacked_reported, email, email_verified, two_factor_enabled, friends, posts, followers, likes)
                print("Password updated successfully.")
            case "4":
                password, role, active, display_name, hacked_reported, email, email_verified, two_factor_enabled, friends, posts, followers, likes = user_database[username]
                while True:
                    new_email = input("| Enter new email address |: ")
                    if not is_valid_email(new_email):
                        print("Invalid email address. Must use the format username@email.com.")
                        continue
                    break
                user_database[username] = (password, role, active, display_name, hacked_reported, new_email, False, two_factor_enabled, friends, posts, followers, likes)
                print("Email updated. Please verify your new email.")
                send_email_code(username, "Email verification")
                verify_email_address(username)
            case "5":
                password, role, active, display_name, hacked_reported, email, email_verified, two_factor_enabled, friends, posts, followers, likes = user_database[username]
                two_factor_enabled = not two_factor_enabled
                user_database[username] = (password, role, active, display_name, hacked_reported, email, email_verified, two_factor_enabled, friends, posts, followers, likes)
                print(f"2-step verification {'enabled' if two_factor_enabled else 'disabled'}.")
            case "6":
                return username
            case _:
                print("Invalid choice. Please try again.")
        print("")


def recover_hacked_account():
    if not admin_notifications:
        print("No hacked account reports available for recovery.")
        return
    print("\nRecoverable hacked accounts:")
    for report_username, display_name in admin_notifications:
        print(f"- {report_username} ({display_name})")
    target = input("| Enter the username to recover |: ")
    if target not in user_database:
        print("Account not found.")
        return
    password, role, active, display_name, hacked_reported, email, email_verified, two_factor_enabled, friends, posts, followers, likes = user_database[target]
    if not hacked_reported:
        print("That account does not have an active hack report.")
        return
    while True:
        new_password = input("| Enter new recovery password |: ")
        is_strong, message = is_strong_password(new_password)
        if is_strong:
            break
        else:
            print(f"Weak password: {message}")
    confirm_password = input("| Confirm new recovery password |: ")
    if new_password != confirm_password:
        print("Passwords do not match. Recovery cancelled.")
        return
    user_database[target] = (new_password, role, True, display_name, False, email, email_verified, two_factor_enabled, friends, posts, followers, likes)
    if target not in active_usernames:
        active_usernames.add(target)
    admin_notifications[:] = [(u, d) for u, d in admin_notifications if u != target]
    print(f"Account {target} has been recovered and the hack report was cleared.")


def admin_actions(username, role):
    while True:
        display_menu(role)
        choice = input("| Enter your choice |: ")
        match choice:
            case "1":
                print("\nAll Users:")
                for user, (pwd, rol, act, display_name, hacked_reported, email, email_verified, two_factor_enabled, friends, posts, followers, likes) in user_database.items():
                    status = "Active" if act else "Inactive"
                    email_status = "Verified" if email_verified else "Unverified"
                    print(f"Username: {user}, Display: {display_name}, Role: {rol}, Status: {status}, Email: {email} ({email_status})")
            case "2":
                print("\nLogged In Users:")
                if logged_in_users:
                    for user in logged_in_users:
                        print(f"Username: {user}, Display: {user_database[user][3]}, Role: {user_database[user][1]}")
                else:
                    print("No users currently logged in.")
            case "3":
                print("\nHacked Account Notifications:")
                if admin_notifications:
                    for report_username, display_name in admin_notifications:
                        print(f"Reported hacked account: {report_username} ({display_name})")
                else:
                    print("No hack reports received.")
            case "4":
                recover_hacked_account()
            case "5":
                logout(username)
                break
            case "6":
                print("Returning to the main menu.")
                break
            case _:
                print("Invalid choice. Please try again.")


def email_management(username):
    while True:
        password, role, active, display_name, hacked_reported, email, email_verified, two_factor_enabled, friends, posts, followers, likes = user_database[username]
        print("\nEmail Management:")
        print(f"Current email: {email}")
        print(f"Verified: {'Yes' if email_verified else 'No'}")
        print("1. Resend verification code")
        print("2. Verify email")
        print("3. Back")
        choice = input("| Enter your choice |: ")
        match choice:
            case "1":
                send_email_code(username, "Email verification")
            case "2":
                verify_email_address(username)
            case "3":
                break
            case _:
                print("Invalid choice. Please try again.")

def search_users(username):
    search_query = input("| Enter username or display name to search |: ").lower()
    print("\nSearch Results:")
    found = False
    for user, (pwd, rol, act, display_name, hacked, email, verified, two_fa, friends, posts, followers, likes) in user_database.items():
        if user != username and (search_query in user.lower() or search_query in display_name.lower()):
            found = True
            print(f"- Username: {user} | Display: {display_name} | Friends: {len(friends)} | Followers: {followers}")
    if not found:
        print("No users found.")


def add_close_friend(username, target):
    password, role, active, display_name, hacked, email, verified, two_fa, friends, posts, followers, likes = user_database[username]
    if target not in friends:
        print(f"{target} is not in your friend list yet.")
        return
    friends.discard(target)
    friends.add(f"{target}:close")
    user_database[username] = (password, role, active, display_name, hacked, email, verified, two_fa, friends, posts, followers, likes)
    print(f"{target} has been marked as a close friend.")


def follow_user(username, target):
    if target not in user_database:
        print("User not found.")
        return
    if target == username:
        print("You cannot follow yourself.")
        return
    password, role, active, display_name, hacked, email, verified, two_fa, friends, posts, followers, likes = user_database[username]
    if target in friends or any(f.startswith(target + ":") for f in friends):
        print("Already following this user.")
        return
    friends.add(target)
    user_database[username] = (password, role, active, display_name, hacked, email, verified, two_fa, friends, posts, followers, likes)
    target_password, target_role, target_active, target_display, target_hacked, target_email, target_verified, target_two_factor, target_friends, target_posts, target_followers, target_likes = user_database[target]
    target_followers += 1
    user_database[target] = (target_password, target_role, target_active, target_display, target_hacked, target_email, target_verified, target_two_factor, target_friends, target_posts, target_followers, target_likes)
    print(f"You are now following {target}.")


def view_friend_list(username):
    password, role, active, display_name, hacked, email, verified, two_fa, friends, posts, followers, likes = user_database[username]
    print("\nFriends & Following:")
    regular_friends = []
    close_friends = []
    for friend in friends:
        if ":close" in friend:
            close_friends.append(friend.replace(":close", ""))
        else:
            regular_friends.append(friend)
    if regular_friends:
        print(f"Following ({len(regular_friends)}):")
        for f in regular_friends:
            print(f"  - {f}")
    if close_friends:
        print(f"Close Friends ({len(close_friends)}):")
        for f in close_friends:
            print(f"  - {f}")
    if not regular_friends and not close_friends:
        print("You are not following anyone yet.")


def social_networking(username):
    while True:
        password, role, active, display_name, hacked, email, verified, two_fa, friends, posts, followers, likes = user_database[username]
        print("\nSocial Networking:")
        print(f"Following: {len(friends)} | Followers: {followers} | Posts: {len(posts)} | Likes: {likes}")
        print("1. Search for users")
        print("2. View friends & following")
        print("3. Follow a user")
        print("4. Add close friend")
        print("5. View your posts")
        print("6. Create a new post")
        print("7. View feed")
        print("8. Back")
        choice = input("| Enter your choice |: ")
        match choice:
            case "1":
                search_users(username)
            case "2":
                view_friend_list(username)
            case "3":
                target = input("| Enter username to follow |: ")
                follow_user(username, target)
            case "4":
                target = input("| Enter username to mark as close friend |: ")
                add_close_friend(username, target)
            case "5":
                password, role, active, display_name, hacked, email, verified, two_fa, friends, posts, followers, likes = user_database[username]
                print(f"\n{display_name}'s Posts:")
                if posts:
                    for index, post in enumerate(posts, start=1):
                        print(f"{index}. {post}")
                else:
                    print("No posts yet.")
            case "6":
                new_post = input("| Enter your post content |: ")
                posts.append(new_post)
                user_database[username] = (password, role, active, display_name, hacked, email, verified, two_fa, friends, posts, followers, likes)
                print("Post added successfully!")
            case "7":
                password, role, active, display_name, hacked, email, verified, two_fa, friends, posts, followers, likes = user_database[username]
                print("\nFeed:")
                feed_posts = []
                for friend in friends | {username}:
                    clean_friend = friend.replace(":close", "")
                    if clean_friend in user_database:
                        _, _, _, friend_display, _, _, _, _, _, friend_posts, _, _ = user_database[clean_friend]
                        for post in friend_posts:
                            feed_posts.append(f"{friend_display}: {post}")
                if feed_posts:
                    for index, post in enumerate(feed_posts, start=1):
                        print(f"{index}. {post}")
                else:
                    print("No feed content available.")
            case "8":
                break
            case _:
                print("Invalid choice. Please try again.")


def user_actions(username, role):
    while True:
        display_menu(role)
        choice = input("| Enter your choice |: ")
        match choice:
            case "1":
                password, role, active, display_name, hacked_reported, email, email_verified, two_factor_enabled, friends, posts, followers, likes = user_database[username]
                status = "Active" if active else "Inactive"
                print(f"\nProfile for {display_name}:")
                print(f"Username: {username}")
                print(f"Display name: {display_name}")
                print(f"Email: {email} ({'Verified' if email_verified else 'Unverified'})")
                print(f"2-step verification: {'Enabled' if two_factor_enabled else 'Disabled'}")
                print(f"Role: {role}")
                print(f"Status: {status}")
                print(f"Friends: {len(friends)} | Followers: {followers} | Posts: {len(posts)} | Likes: {likes}")
                print(f"Hack report sent: {'Yes' if hacked_reported else 'No'}")
            case "2":
                username = account_management(username)
            case "3":
                email_management(username)
            case "4":
                social_networking(username)
            case "5":
                send_hack_alert(username)
            case "6":
                logout(username)
                break
            case "7":
                print("Returning to the main menu.")
                break
            case _:
                print("Invalid choice. Please try again.")


def hacker_simulator():
    print("\n==========================")
    print("    -| Hacker Simulator |-  ")
    print("============================")
    print("Available accounts to infiltrate:")
    for user, (_, _, active, display_name, _, _, _, _, _, _, _, _) in user_database.items():
        status = "Active" if active else "Inactive"
        print(f"- {user} ({display_name}) [{status}]")
    target = input("| Enter the username to simulate hack |: ")
    if target not in user_database:
        print("Account not found.")
        return
    if not user_database[target][2]:
        print("This account is inactive and cannot be targeted.")
        return
    print(f"Simulating account infiltrate for {target}...")
    send_hack_alert(target)


def main():
    print("--------------------------------------------------------")
    print("  -| Welcome to the Official Authentication System |-  ")
    print("--------------------------------------------------------")

    while True:
        print("\nMain Menu:")
        print("1. Login")
        print("2. Register")
        print("3. Hacker Simulator")
        print("4. Exit")
        choice = input("| Enter your choice |: ")
        match choice:
            case "1":
                username, role = login()
                if username:
                    if role == "admin":
                        admin_actions(username, role)
                    else:
                        user_actions(username, role)
            case "2":
                register()
            case "3":
                hacker_simulator()
            case "4":
                print("Exiting system.")
                exit()
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
            
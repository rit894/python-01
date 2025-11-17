'''In cybersecurity, an Access Control List (ACL) defines who is allowed to access a specific system. Security
 analysts often compare logs of users who attempted to login against the list of users who are actually
 authorized.
 Write a function called identify
 intruders. It accepts two arguments:
 • attempts: A list of usernames that tried to log in.
 • authorized: A set of usernames that are allowed access.
 The function should return a set containing only the usernames from attempts that are NOT in the
 authorized set'''
login_attempts = ["alice", "bob", "eve", "alice", "mallory", "frank", "eve"]
authorized_users = {"alice", "bob", "frank", "grace"}
def identify(login_attempts,authorized_users):
    print(set(login_attempts)-authorized_users)

identify(login_attempts,authorized_users)


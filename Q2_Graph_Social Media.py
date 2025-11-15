
# 1. Directed Graph (Unweighted)
class UDGraph: #adjacency list
    def __init__(self):
        self.graph = {}   # vertex → list of outgoing adjacent vertices

    def add_vertex(self, vertex):  #Add a new vertex(user) to the graph
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, start, end): #undirected edge connect start and end vertices
        if start in self.graph and end in self.graph: #Follow
            self.graph[start].append(end)
        else:
            print("One or both vertices do not exist.")

    def list_outgoing_adjacent(self, vertex): #list user follow who
        if vertex in self.graph:
            return self.graph[vertex]
        return []

    def list_incoming_adjacent(self, vertex):#list user followers
        followers = []
        for v in self.graph:
            if vertex in self.graph[v]:
                followers.append(v)
        return followers


# 2. Person Class (Domain Entity)
class Person:#class to save user information
    def __init__(self, username, gender, bio, privacy="public"):
        self.username = username
        self.gender = gender
        self.bio = bio
        self.privacy = privacy  # "public" or "private"

    def __str__(self):
        if self.privacy == "private": #only show name
            return f"Name: {self.username}\n(Private Account – Details Hidden)"
        else:
            return (f"Name: {self.username}\n" #public settings show everything
                    f"Gender: {self.gender}\n"
                    f"Bio: {self.bio}\n"
                    f"Privacy: {self.privacy}")


# 3. Create People
people = {
    "Jessie": Person("Jessie", "Female", "Love traveling", "public"),
    "Susy": Person("Susy", "Female", "Coffee lover", "public"),
    "Teddy": Person("Teddy", "Male", "Gamer", "public"),
    "Elmo": Person("Elmo", "Male", "Engineer", "private"),
    "Mike": Person("Mike", "Male", "Music fan", "public"),
}

# 4. Create Graph & Add Vertices
social = UDGraph()  #set social value to hold the UDGraph

for username in people:
    social.add_vertex(username)

# Sample following data
social.add_edge("Jessie", "Susy") #Jessie follow Susy
social.add_edge("Jessie", "Teddy")
social.add_edge("Jessie", "Elmo")
social.add_edge("Elmo", "Mike")
social.add_edge("Teddy", "Jessie")


# 5. Menu-Driven Program
def main():
    choice = 0
    while choice != 8:
        print("\n*****Social Media*****")
        print("1. Display all users")
        print("2. View a user's profile")
        print("3. View accounts a user follows (outgoing edges)")
        print("4. View followers of a user (incoming edges)")
        print("5. Add a new user")
        print("6. Follow someone")
        print("7. Unfollow someone")
        print("8. Exit")
        print("*************************")

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Invalid input. Enter a number.")
            continue

        # 1. Display all usernames
        if choice == 1:
            print("\nAll Users:")
            for username in people:
                print("-", username)

        # 2. View profile
        elif choice == 2:
            name = input("Enter username: ")
            if name in people:
                print("\nProfile:")
                print(people[name])
            else:
                print("User not found.")

        # 3. Outgoing edges (following)
        elif choice == 3:
            name = input("Enter username: ")
            if name in social.graph:
                following = social.list_outgoing_adjacent(name)
                print(f"\n{name} follows: {following}")
            else:
                print("User not found.")

        # 4. Incoming edges (followers)
        elif choice == 4:
            name = input("Enter username: ")
            if name in social.graph:
                followers = social.list_incoming_adjacent(name)
                print(f"\n{name} is followed by: {followers}")
            else:
                print("User not found.")

        # 5. Add new user
        elif choice == 5:
            username = input("New username: ")
            gender = input("Gender: ")
            bio = input("Bio: ")
            privacy = input("Privacy (public/private): ")

            people[username] = Person(username, gender, bio, privacy)
            social.add_vertex(username)
            print("User added successfully.")

        # 6. Follow someone
        elif choice == 6:
            a = input("Follower username: ")
            b = input("User to follow: ")
            social.add_edge(a, b)
            print(f"{a} now follows {b}.")

        # 7. Unfollow someone
        elif choice == 7:
            a = input("Username: ")
            b = input("Unfollow who: ")

            if a in social.graph and b in social.graph[a]:
                social.graph[a].remove(b)
                print(f"{a} unfollowed {b}.")
            else:
                print("Invalid relationship.")

        elif choice == 8:
            print("Exiting program. Bye!")

        else:
            print("Invalid choice.")

# Run Program
main()

class Person:
    """A person in the social network."""

    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        # Avoid duplicate friendships and friending yourself.
        if friend is not self and friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    """A social network stored as an adjacency list."""

    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"Person not added. {name} already exists!")
            return

        self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return

        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return

        if person1_name == person2_name:
            print("Friendship not created. A person cannot friend themselves!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        # Add both sides because the friendship is bidirectional.
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for person in self.people.values():
            friend_names = [friend.name for friend in person.friends]
            friends_text = ", ".join(friend_names) if friend_names else "No friends yet"
            print(f"{person.name} is friends with: {friends_text}")


if __name__ == "__main__":
    network = SocialNetwork()

    # Add six people.
    for name in ["Alex", "Jordan", "Morgan", "Taylor", "Casey", "Riley"]:
        network.add_person(name)

    # Add eight friendships.
    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    # Try the edge cases.
    network.add_friendship("Jordan", "Johnny")  # Johnny is not in the network.
    network.add_person("Alex")                 # Alex is already in the network.
    network.add_friendship("Alex", "Jordan")   # Does not add a duplicate.
    network.add_friendship("Alex", "Alex")     # A person cannot friend themselves.

    # Check that there are six people and eight two-way friendships.
    assert len(network.people) == 6
    assert sum(len(person.friends) for person in network.people.values()) == 16

    print("\nFinal network:")
    network.print_network()


# DESIGN MEMO
# A graph is the right choice for a social network because each person can
# connect to many other people. I represent each person as a node and each
# friendship as an edge. The friendships go both ways, so when Alex is
# connected to Jordan, the program stores both connections. Each Person
# stores a list of their friends, which is an adjacency list.
#
# A regular list could hold all the users, but it would not show who is
# connected to whom by itself. I would need extra information to find each
# person's friendships. A tree is also not a good fit because trees are
# organized into parent and child branches. In a social network, people can
# have many friends, share friends, and form cycles.
#
# One trade-off is that checking if someone is already a friend takes time
# because the program searches that person's friend list. Adding a friendship
# checks both lists and stores the connection twice so both people can see it.
# The dictionary makes finding a person by name quick on average, but names
# need to be unique. Printing takes longer as the network grows because the
# program visits every person and each friendship. This design works for a
# small network, but a larger platform would need unique user IDs and a
# database.
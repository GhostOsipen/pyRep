from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thomy", "jonny_m"]
graph["anuj"] = []
graph["peggy"] = []
graph["thomy"] = []
graph["jonny_m"] = []

def person_is_seller(person):
    if person[-1] == "m":
        return True

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")
conversation = []


def add_message(role, content):
    conversation.append({"role": role, "content": content})


def get_recent_messages(limit=5):
    return conversation[-limit:]


# 1. Add 10 messages (5 conversation turns)
add_message("user", "What is Python?")
add_message("assistant", "Python is a high-level programming language.")

add_message("user", "What are variables?")
add_message("assistant", "Variables store data values.")

add_message("user", "What are functions?")
add_message("assistant", "Functions are reusable blocks of code.")

add_message("user", "Explain loops.")
add_message("assistant", "Loops iterate over a sequence of elements.")

add_message("user", "What is a list?")
add_message("assistant", "A list is an ordered, mutable collection of items.")

# 2. Retrieve only the last 5 messages
context = get_recent_messages(5)

# 3. Print total stored messages
print(f"Total stored messages: {len(conversation)}")

# 4. Print number of messages sent to LLM
print(f"Messages sent to LLM: {len(context)}\n")

print("Context sent to LLM:\n")
for message in context:
    print(f"{message['role']}: {message['content']}")
import datetime
import webbrowser


def voice_assistant():
    print("Hello! I am your Python Assistant. How can I help you today?")

    while True:
        command = (
            input("\nEnter your command (or type 'exit' to quit): ")
            .lower()
            .strip()
        )

        if "hello" in command:
            print("Assistant: Hello! Hope you are having a great day.")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Assistant: The current time is {current_time}")

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            print(f"Assistant: Today's date is {current_date}")

        elif "search" in command:
            query = command.replace("search", "").strip()
            if query:
                print(f"Assistant: Searching Google for '{query}'...")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            else:
                print("Assistant: What do you want me to search for?")

        elif "exit" in command or "bye" in command:
            print("Assistant: Goodbye! Have a nice day.")
            break
        else:
            print(
                "Assistant: Sorry, I didn't understand that. Try 'hello', 'time', 'date', or 'search [query]'."
            )


# Assistant ko run karne ke liye
if __name__ == "__main__":
    voice_assistant()
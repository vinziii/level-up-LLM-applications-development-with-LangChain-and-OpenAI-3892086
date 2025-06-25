from dotenv import load_dotenv
import os
# from langchain_openai import OpenAI
from langchain.chat_models import init_chat_model
from colorama import Fore
from langchain_core.prompts import PromptTemplate



# Load environment variables
load_dotenv()

# Make sure the API key is set in the environment
api_key = os.getenv("OPENAI_API_KEY", "")
os.environ["OPENAI_API_KEY"] = api_key

# Initialize OpenAI with a simple configuration
# llm = OpenAI(temperature=0.7)
llm = init_chat_model("gpt-4o-mini", model_provider="openai")


prompt_template = PromptTemplate.from_template("Tell me a joke about {topic}")


def generate(text):
    """ generate text based on the input """
    prompt = prompt_template.format(topic=text)
    print(prompt)
    return llm.invoke(text)

def start():
    instructions = (
        "Type your question and press ENTER. Type 'x' to go back to the MAIN menu.\n"
    )
    print(Fore.BLUE + "\n\x1B[3m" + instructions + "\x1B[0m" + Fore.RESET)

    print("MENU")
    print("====")
    print("[1]- Ask a question")
    print("[2]- Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        ask()
    elif choice == "2":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice")
        start()


def ask():
    while True:
        user_input = input("Q: ")
        # Exit
        if user_input == "x":
            start()
        else:
            response = generate(user_input)
            # Extract the content from the AIMessage object
            response_text = response.content if hasattr(response, 'content') else str(response)
            print(Fore.BLUE + f"A: " + response_text + Fore.RESET)
            print(Fore.WHITE + "\n-------------------------------------------------")


if __name__ == "__main__":
    start()

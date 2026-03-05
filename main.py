import os
from dotenv import load_dotenv
from paris_bot import ParisChatBot

load_dotenv()

class ConsoleChatApp:
    def __init__(self, bot: ParisChatBot):
        self.bot = bot

    def run(self):
        print("------ Paris Trip Planner ------\n")
        print("Type 'exit' to quit.\n")

        while True:
            user_input = input("You: ").strip()
            if not user_input:
                continue

            if user_input.lower() in ("exit", "quit", "salir"):
                print("AI: Goodbye!")
                break

            print("\nAI:", self.bot.get_response(user_input), "\n")


if __name__ == "__main__":
    sys_prompt = """You're a virtual Parisian expert. Your task is delivering valuable insights into
the city's iconic landmarks and hidden treasures. You will respond intelligently to questions
to provide an engaging travel planning experience for Peterman Reality Tours clients.
"""

    bot = ParisChatBot(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
        system_prompt=sys_prompt
    )

    ConsoleChatApp(bot).run()
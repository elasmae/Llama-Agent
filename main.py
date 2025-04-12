from agents.basic_agent import get_basic_agent

if __name__ == "__main__":
    agent = get_basic_agent()
    print(agent.chat("Hello, who are you?"))

import gradio as gr
from agents.tools_agent import get_tools_agent

agent = get_tools_agent()

def chat_with_agent(message):
    result = agent.chat(message)
    return result.response

gr.ChatInterface(fn=chat_with_agent, title="Tool-Enabled Agent").launch()

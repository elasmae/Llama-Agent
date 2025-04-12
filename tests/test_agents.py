from agents.basic_agent import get_basic_agent

def test_basic_agent_response():
    agent = get_basic_agent()
    assert agent is not None

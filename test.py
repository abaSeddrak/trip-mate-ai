from tools.tavily_tool import tavlily_tool
from backend import run_travel_agent

if __name__ =="__main__":
  result = run_travel_agent(

    user_input="to kuwait",
    thread_id="abaoub"
  )
  print(result["answer"])
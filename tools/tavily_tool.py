from tavily import TavilyClient
import os
from dotenv import load_dotenv
client = TavilyClient(
    os.getenv("TAVILY_API_KEY")
)
def tavlily_tool(query:str):
   response = client.search(
        query=query,
        max_results=3
    )
   
   result = []
   for i,r in enumerate(response["results"],1):
       title= r.get("title","unkonown")
       url=r.get("url","")
       content=r.get("content","").strip()
       
       result.append(f"{i} {title} {url} {content}")
       
       
   return " ".join(result)



   
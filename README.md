A powerful AI chatbot that leverages GROQ LLM, Tavily Search, and a REACT agent to answer user queries with intelligence and real-time information. This project demonstrates how tool-based agents can enhance chatbot capabilities by integrating search results dynamically.

Tech Stack
GROQ LLM: (llama-3.3-70b-versatile) – Handles conversational tasks with advanced text generation.

Tavily Search API: Fetches real-time search results to keep answers updated.

LangChain & LangGraph: Used to create and manage the REACT agent.

dotenv: Secure API key handling.

 Project Setup
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yogesh-bhattarai/Agentic_AI_chatbot.git  
cd Agentic_AI_chatbot  
2. Install Dependencies
Make sure you have Python installed, then run:

bash
Copy
Edit
pip install -r requirements.txt  
3. Set Up Environment Variables
Create a .env file in the project root and add the following keys:

bash
Copy
Edit
GROQ_API_KEY=your_groq_api_key  
TAVILY_API_KEY=your_tavily_api_key  
4. Run the Chatbot
bash
Copy
Edit
python chatbot.py  
How It Works
Initialize the GROQ LLM to handle text-based conversations.

Integrate Tavily Search to fetch 2 real-time search results per query.

Create the REACT Agent to manage dynamic tool usage and state handling.

Process User Queries and return intelligent, context-aware answers.

 Use Cases
Personalized Q&A: Answer any query with AI-powered intelligence.

Research and Education Tool: Fetch real-time information for deeper insights.

AI Assistant: Acts as a dynamic assistant with real-time search integration.

Future Enhancements
Add more tools (e.g., Wikipedia API, calculator).

Improve multi-turn conversation handling.

Fine-tune the LLM for specific domains.

Feedback and Contributions
I’d love to hear your feedback or ideas! Feel free to contribute by opening a pull request or raising an issue.

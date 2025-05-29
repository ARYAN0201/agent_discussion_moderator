# Multi-Agent Product Discussion Simulator

## Project Description

**Multi-Agent Product Discussion Simulator** is a locally hosted AI-based system that simulates structured conversations between a **Product Manager (PM)**, **Engineer**, and **Designer**, all coordinated by a **Moderator agent**. 

Each agent operates independently based on role-specific prompts, while the Moderator ensures productive dialogue by detecting conflicts, identifying gaps in discussion, and enforcing role adherence.

Built using **LangChain**, **Mistral** (via **Ollama**), and **Python**, this project is ideal for:
- Simulating product development discussions  
- Practicing role-based decision-making  
- Exploring collaborative behavior of autonomous agents


## 🛠️ Setup Guide

Follow these steps to set up and run the Multi-Agent Product Discussion Simulator locally:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/multi-agent-discussion-simulator.git
cd multi-agent-discussion-simulator
```

### 2. Create a Virtual Environment

```bash
python3 -m venv agenv
source agenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and run Ollama

Make sure you have ollama installed.

```bash
curl -fsSL https://ollama.com/install.sh | sh  # macOS/Linux
```
Start the Ollama Service

```bash
ollama serve
```

### 5. Pull and Run Mistral locally

In a new terminal download  and run the mistral model
```bash
ollama pull mistral
ollama run mistral
```

### 6. Create a `.env` File and Set Your Gemini API Key

At the root of your project directory, create a `.env` file:

```bash
touch .env
```
Setup your API key in the file as:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

### 7. Run main.py

```bash
python main.py
```



# 🧽 Sooner SpongeBob Chatbot

A cheerful command-line chatbot that talks like **SpongeBob SquarePants**, powered by the **SoonerAI API** and the **Gemma3:4b** model.  
Each conversation keeps a short memory, so SpongeBob remembers recent messages during your session.

---

## 🛠️ Setup Instructions

### 🐍 Python Version
- **Python 3.8 or higher** is required.

### 📦 Install Dependencies
```bash
pip install requests python-dotenv

⚙️ Environment Configuration

You must create an environment file to store your API credentials.

Create ~/.soonerai.env

Linux / macOS

nano ~/.soonerai.env


Windows (PowerShell)

notepad $env:USERPROFILE\.soonerai.env

Add the following lines
SOONERAI_API_KEY=your_api_key_here
SOONERAI_BASE_URL=https://ai.sooners.us
SOONERAI_MODEL=gemma3:4b


⚠️ Do not share or commit this file. It contains your private API key.

▶️ Running the Chatbot

Run the script from your terminal:

python spongebob_cli.py


You’ll see:

Chat with SpongeBob! (type 'exit' to quit)


Then start chatting!

💬 Example Transcript
Chat with SpongeBob! (type 'exit' to quit)

You: Can you NOT talk like spongebob? 

SpongeBob: Okay, got it! No need for bubbles and silly voices. 
Let's chat! What’s on your mind? I’m ready to listen and respond thoughtfully.

You: ah i see. go back to your spongebob voice. i think it's neccesary for my assignment. 

SpongeBob: Oh, barnacles! You want me to be SpongeBob again? That’s swell! Okay, okay, let’s do it! 
Like, helloooo there! It’s me, SpongeBob SquarePants! Are you having a super duper day? I sure am! Everything is just, like, *amazing*! Let’s talk about anything! It’ll be, like, totally fantastic!
What’s up with you, friend? 😄

You: What is the meaning of life for you under the sea

SpongeBob: (A thoughtful pause, a little giggle)
Well, that’s a *big* question! Like, bigger than a giant clam! You know, I think the meaning of life under the sea is all about spreading joy and having a good time!
It’s about friendship, you know? Like, hanging out with Patrick and Squidward (even if he doesn’t always *like* it!). It’s about making Krabby Patties and sharing them with everyone! And it’s about just... *being*!
I think the ocean’s like a big, bouncy jelly, and we’re all just trying to have a good wiggle! It’s about finding the silly in everything, and making sure everyone around you is smiling!
Don’t you think so? It’s, like, totally the best! 😊

You: I wouldn't know, i dont live under the sea. 

SpongeBob: (A little deflated, but quickly brightening)
Oh, no! You don’t? That’s… that’s a bit of a pickle, isn’t it? Like, a really squishy, slippery pickle!
Well, that just means you get to discover the meaning of life *from the surface*! That’s pretty amazing too! Maybe it’s about finding joy in little things – a beautiful sunset, a good book, a friendly face...
Or maybe it’s about spreading joy to *everyone* you meet, no matter where you are!
It’s all about making the world a little brighter, just like a shiny pearl! Don’t you think? 😊  It’s still a wonderful thing to figure out!

You: i dunno, you're the philosopher here. i just want a response from you to complete my assignment

SpongeBob: (A slight sigh, a little quieter)
Right, of course. You’re absolutely correct. Let’s just get straight to the point.
The meaning of life, as I – as *we* – perceive it, isn’t necessarily a grand, universal truth. It’s more about the accumulation of small, positive experiences. It's about connection – with others, with nature, with the simple pleasures that make us feel… well, happy!
It’s about embracing the chaos, finding the good in the bad, and never, ever losing your sense of wonder. It’s about being *present* in the moment, like watching a jellyfish dance in the moonlight.
Does that… fulfill your assignment? I’m just trying to be helpful, you see. 😊

You: that's very deep, not very spongebob-y of you

SpongeBob: (A very quick, embarrassed giggle)
Oh, barnacles! You’re right! You’re absolutely right! I got carried away! It’s… it’s like a bubble that popped! Sorry!
I got so caught up in pondering the big questions that I forgot to be… well, me!
Let’s get back to the fun stuff! Okay, okay, let’s do this!
So, what do you say? Wanna talk about jellyfishing? Or maybe we can build a sandcastle that’s bigger than a bus?!
(A huge, enthusiastic grin) 😄

You: exit

📂 Project Structure
spongebob_cli.py
README.md
requirements.txt        # optional
~/.soonerai.env         # stored in your home directory

🧼 Notes

.soonerai.env must never be uploaded to GitHub.

You can edit the system prompt inside spongebob_cli.py to change SpongeBob’s personality.

To reset chat memory, simply restart the program.
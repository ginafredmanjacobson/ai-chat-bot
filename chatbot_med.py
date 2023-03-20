import openai

openai.api_key ="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"

messages = []
syst_msg = input("What kind of chatbot would you like to create?\n")
messages.append({"role": "system", "content": syst_msg})

print("Your new chatbot is ready for use!")
while input != "quit()":
    message = input("")
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choice"][0]["message"]["content"]
    messages.append({"role": "chatbot", "content": reply})
    print("\n" + reply + "\n")
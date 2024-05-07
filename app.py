import chainlit as cl

@cl.on_message
async def on_message(message: cl.Message):
    await cl.Message(
        content=f"Received: {message.content}"
    ).send()
    
@cl.on_chat_start
async def on_chat_start():
    await cl.Message(
        content=f"Hi, fam! I am libra tiger from US. Feel free to ask anything you want to know. Let me do the best for you guys."
    ).send()
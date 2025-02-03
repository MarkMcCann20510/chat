from uuid import uuid4
from nicegui import ui

messages = []

@ui.refreshable
def chat_messages(own_id)
  for user_id, avatar, text in messages:
      ui.chat_messages(avatar=avatar, text=text, sent=user_id==own_id)

@ui.page('/')
def index():
    def send():
        messages.append((user, avatar, text.value))
        chat_message.refresh()
        text.value = ''

    user = str(uuid4())
    avatar = f'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkM3ZK8QC0-7bKCoV0wg5wRrOjByhBtRvfwg&s'
    with ui.column().classes('w-full items-stretch'):
        chat_messages(user)

    with ui.footer().classes('bg-white'):
        with ui.row().classes('w-full items-center'):
            with ui.avatar():
                ui.image(avatar)
            text = ui.input(placeholder='message') \
                .props('rounded outlined').classes('flex-grow') \
                .on('keydown.enter', send)

  ui.run()
    

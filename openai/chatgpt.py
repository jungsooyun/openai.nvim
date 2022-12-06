import os

import openai
import neovim


CONFIG_PATH = '~/.openai-key'


# Define the Neovim plugin
@neovim.plugin
class OpenAIChatGPTPlugin:
    def __init__(self, nvim):
        self.nvim = nvim
        if not os.path.exists(CONFIG_PATH):
            self.nvim.write(f'error: {CONFIG_PATH} not exists')

    # Define the Neovim command that will be called by the plugin
    @neovim.command("ChatGPT", range=".", nargs="*", sync=True)
    def openai_chat_gpt(self, args, range):
        # Get the current buffer
        buffer = self.nvim.current.buffer

        # Get the current line
        line = buffer[range[0]]

        # Use the OpenAI Chat GPT API to generate text based on the current line
        response = openai.Completion.create(
            engine="chat",
            prompt=line,
            max_tokens=1024,
            temperature=0.5,
        )

        # Get the generated text from the API response
        text = response["choices"][0]["text"]

        # Write the generated text to the Neovim buffer
        buffer[range[0]] = text

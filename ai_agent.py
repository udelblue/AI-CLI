import openai
import configparser
from colorama import Fore, Style, init



def call_ai_agent(prompt, system_message=None, model=None , max_tokens=None , verbose=False ):
    
    # Load API key from properties file
    config = configparser.ConfigParser()
    config.read('config.properties')
    api_key = config.get('API', 'key', fallback=None)
    
    # Load default model from properties file and override if model is provided
    if model is None:
        default_model = config.get('CONFIG', 'default_model', fallback=None)
    else:
        default_model = model

    if max_tokens is None:
        max_tokens = config.get('CONFIG', 'max_tokens', fallback=None)  
    else:
        max_tokens = max_tokens

    if verbose:
            print(Style.RESET_ALL + Fore.GREEN + "Verbose mode is enabled.")
            print(Fore.YELLOW + f"Prompt file: {prompt}")
            print(Fore.YELLOW + f"Model: {default_model}")
            print(Fore.YELLOW + f"Max tokens: {max_tokens}")
            print(Fore.YELLOW + f"Prompt message: {prompt}")
            if system_message:
                print(Fore.YELLOW + f"System message: {system_message}")


    if not api_key:
        return print(Fore.RED + f"Error: API key not found in config.properties.") 

    # Set up OpenAI API key
    openai.api_key = api_key

    
    try:

        if system_message:
            # Call the AI agent (e.g., OpenAI GPT) with a system message
            response = openai.chat.completions.create(
                model= str(default_model),
                messages=[{"role": "system", "content": system_message}, {"role": "user", "content": prompt}],
                max_tokens=int(str(max_tokens))
            )
        else:   
            # Call the AI agent (e.g., OpenAI GPT) without a system message
            response = openai.chat.completions.create(
                model= str(default_model),
                messages=[{"role": "user", "content": prompt}],
                max_tokens=int(str(max_tokens))
            )

        # Call the AI agent (e.g., OpenAI GPT)
        response = openai.chat.completions.create(
            model= str(default_model),
            messages=[{"role": "user", "content": prompt}],
            max_tokens=int(str(max_tokens))
        )
        # Extract the response content
        if not response.choices or len(response.choices) == 0:
            return print(Fore.RED + f"Error: No response from AI agent.") 
        
        # Return the AI's response  
        model_response = response.choices[0].message.content


        return model_response
    except Exception as e:
        return print(Fore.RED + f"Error calling AI agent: {e}")
    
    
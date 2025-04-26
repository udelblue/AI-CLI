import openai
import configparser
from colorama import Fore, Style, init
from typing import Iterable



def call_ai_agent(prompt, system_message=None, model=None , max_tokens=None , verbose=False, temperature=0 , top_p=1, return_json=False , openai_api_key=None): 
    """
    Call the AI agent (e.g., OpenAI GPT) with the provided prompt and parameters.
    Args:
        prompt (str): The prompt to send to the AI agent.
        system_message (str, optional): A system message to provide context. Defaults to None.
        model (str, optional): The model to use. Defaults to None.
        max_tokens (int, optional): The maximum number of tokens in the response. Defaults to None.
        verbose (bool, optional): Whether to print verbose output. Defaults to False.
        temperature (float, optional): Sampling temperature. Defaults to 0.
        top_p (float, optional): Nucleus sampling parameter. Defaults to 1.
        return_json (bool, optional): Whether to return the response as JSON. Defaults to False.
        openai_api_key (str, optional): OpenAI API key. Defaults to None.


    Returns:
        str: The AI agent's response.
    """

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

    # set openai_api_key if one is provided from cli
    if openai_api_key:
        api_key = openai_api_key

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
                max_tokens=int(str(max_tokens)),
                temperature=temperature,
                top_p=top_p
                
            )
        else:   
            # Call the AI agent (e.g., OpenAI GPT) without a system message
            response = openai.chat.completions.create(
                model= str(default_model),
                messages=[{"role": "user", "content": prompt}],
                max_tokens=int(str(max_tokens)),
                temperature=temperature,
                top_p=top_p
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
        if return_json:
            model_response = response.choices[0].model_dump_json()
        else:
            model_response = response.choices[0].message.content


        # Print the response if verbose mode is enabled
        if verbose:
            print(Style.RESET_ALL + Fore.GREEN + "Verbose mode is enabled.")
            print(Fore.BLUE + f"Prompt: {prompt}")
            print(Fore.WHITE + f"Response: {model_response}")
            print(Fore.YELLOW + f"Model: {default_model}")
            print(Fore.YELLOW + f"Max tokens: {max_tokens}")
            print(Fore.YELLOW + f"Temperature: {temperature}")
            print(Fore.YELLOW + f"Top P: {top_p}")
            if system_message:
                print(Fore.YELLOW + f"System message: {system_message}")

        return model_response
    except Exception as e:
        return print(Fore.RED + f"Error calling AI agent: {e}")
    
    
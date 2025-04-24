import argparse
from colorama import Fore, Style, init
from ai_agent import call_ai_agent
import os


# Initialize colorama
init(autoreset=True)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(prog='AI-CLI',description="A CLI tool to interact with an AI agent.")
    parser.add_argument(
        "--prompt_file", 
        type=str, 
        required=True, 
        default=None,
        help="Path to the file containing the prompt text."
    )

    parser.add_argument(
        "--output_file", 
        type=str, 
        required=True, 
        default=None,
        help="Path to the file where the AI response will be saved."
    )

    parser.add_argument(
        "--model", 
        type=str, 
        required=False, 
        default=None,
        choices=["gpt-4", "gpt-4-0314", "gpt-4-32k", "gpt-4-32k-0314", "gpt-3.5-turbo", "gpt-3.5-turbo-0301", "text-davinci-003", "code-davinci-002", "text-davinci-001", "text-curie-001", "text-babbage-001", "text-ada-001"],
        help="Model used. Default is set in the config file."
    )

    parser.add_argument(
        "--system_message_file", 
        type=str, 
        required=False, 
        help="Path to the file containing the System message."
    )

    parser.add_argument(
        "--openai_api_key", 
        type=str, 
        required=False, 
        default=None,
        help="OpenAI api key. If passed it will ignore the one in the config file."
    )


    parser.add_argument(
        "--max_tokens", 
        type=int, 
        required=False, 
        help="Limits the number of tokens in the response. Default is set in the config file."
    )

    parser.add_argument(
        "--temperature", 
        type=int, 
        required=False, 
        default=0,
        help="Controls randomness. Lower values make output more deterministic."
    )

    parser.add_argument(
        "--top_p", 
        type=int, 
        required=False, 
        default=1,
        help="Controls diversity via nucleus sampling. 0.5 means half of all likelihood-weighted options are considered."
    )

    parser.add_argument(
        "--verbose", 
        type=bool, 
        required=False, 
        default=False,
        choices=[True, False],
        help="Verbose mode. Extra information will be printed to the console. Good for debugging."
    )

    parser.add_argument(
        "--return_json", 
        type=bool, 
        required=False, 
        default=False,
        choices=[True, False],
        help="Return JSON format of responses."
    )


    parser.add_argument(
        "--prompt_prepend_file", 
        type=str, 
        required=False, 
        default=None,
        help="Path to the file containing the prompt prepend text."
    )

    args = parser.parse_args()

    # Read the system message from the file
    system_message = None
    system_message_file = args.system_message_file

    # Check if the system message file is provided
    if system_message_file:
        try:
            with open(system_message_file, 'r') as file:
                system_message = file.read()
        except FileNotFoundError:
            print(Fore.RED + f"Error: The file {system_message_file} was not found.")
            return
    

    # Read the prompt from the file
    try:
        with open(args.prompt_file, 'r') as file:
            prompt = file.read()
    except FileNotFoundError:
        print(Fore.RED + f"Error: The file {args.prompt_file} was not found.")
        return

    # Read the prompt prepend from the file
    prepend_file = args.prompt_prepend_file

    if prepend_file:
        try:
            with open(prepend_file, 'r') as file:
                prepend = file.read()
                prompt = prepend + " " + prompt
        except FileNotFoundError:
            print(Fore.RED + f"Error: The file {prepend_file} was not found.")
            return


    # get the model
    # Check if the model is provided
    model = args.model

    # get the verbose flag
    verbose = args.verbose

    # get the max tokens
    max_tokens=args.max_tokens

    # temperature value
    temperature=args.temperature

    # top_p value
    top_p=args.top_p

    # return_json flag
    return_json=args.return_json

    # Call the AI agent
    response = call_ai_agent(prompt=prompt, model=model , system_message=system_message, verbose=verbose , max_tokens=max_tokens, temperature=temperature, top_p=top_p, return_json=return_json , openai_api_key=args.openai_api_key)

    # Write the response to the output file
    try:
        with open(args.output_file, 'w') as file:
            file.write(str(response))
        if verbose:
            print(Fore.YELLOW + f"Input file path: {args.prompt_file}")
            print(Fore.YELLOW + f"Output file path: {args.output_file}")
            print(Fore.GREEN + f"Response successfully written to {args.output_file}")
    except Exception as e:
        print(Fore.RED + f"Error writing to file: {e}")

if __name__ == "__main__":
    main()

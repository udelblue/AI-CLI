import argparse
from colorama import Fore, Style, init
from ai_agent import call_ai_agent

# Initialize colorama
init(autoreset=True)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(prog='AI-CLI',description="A CLI tool to interact with an AI agent.")
    parser.add_argument(
        "--prompt_file", 
        type=str, 
        required=True, 
        help="Path to the file containing the prompt text."
    )

    parser.add_argument(
        "--output_file", 
        type=str, 
        required=True, 
        help="Path to the file where the AI response will be saved."
    )

    parser.add_argument(
        "--model", 
        type=str, 
        required=False, 
        help="Model used. Default is set in the config file."
    )

    parser.add_argument(
        "--system_message_file", 
        type=str, 
        required=False, 
        help="Path to the file containing the System message."
    )

    parser.add_argument(
        "--max_tokens", 
        type=int, 
        required=False, 
        help="Max tokens used in the api call. Default is set in the config file."
    )

    parser.add_argument(
        "--verbose", 
        type=bool, 
        required=False, 
        help="Verbose mode. Extra information will be printed to the console. Good for debugging."
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

    # get the model
    # Check if the model is provided
    model = args.model

    # get the verbose flag
    verbose = args.verbose

    # get the max tokens
    max_tokens=args.max_tokens


    # Call the AI agent
    response = call_ai_agent(prompt=prompt, model=model , system_message=system_message, verbose=verbose , max_tokens=max_tokens)

    # Write the response to the output file
    try:
        with open(args.output_file, 'w') as file:
            file.write(str(response))
        if verbose:
            print(Fore.GREEN + f"Response successfully written to {args.output_file}")
    except Exception as e:
        print(Fore.RED + f"Error writing to file: {e}")

if __name__ == "__main__":
    main()

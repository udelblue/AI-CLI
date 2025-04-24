
# AI-CLI
AI CLI is a commandline utility to batch process files through a openai model. 


## Install uv 

uv pip install -e

## Set key

Set the openapi key in the config.properties file
key=sk-******************************

## Command line options

python main.py --help

## Run 

python main.py --prompt_file [input_file] --output_file [output_file] 

### Example prompts

python main.py --prompt_file example_prompts/example_joke.prompt --output_file  example_output/example_output.txt  --verbose=True

python main.py --prompt_file example_prompts/example_joke.prompt --output_file  example_output/example_output.txt --system_message_file example_system_messages/role_comedian.prompt --verbose=True
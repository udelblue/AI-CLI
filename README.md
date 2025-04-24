
# AI-CLI
AI CLI is a commandline utility to batch process files through a openai model. 

## Install uv 

```bash
uv pip install -e
```

## Set key

Set the openapi key in the config.properties file
key=sk-******************************

## Run 

```bash
python main.py --prompt_file [input_file] --output_file [output_file] 
```

### Example prompts

```bash
python main.py --prompt_file example_prompts/example_joke.prompt --output_file  example_output/example_output.txt  --verbose=True
```

```bash
python main.py --prompt_file example_prompts/example_joke.prompt --output_file  example_output/example_output.txt --system_message_file example_system_messages/role_comedian.prompt --verbose=True
```

## Command line options
```bash
python main.py -h
```

### Options:
```bash
  -h, --help            show this help message and exit

  --prompt_file PROMPT_FILE
                        Path to the file containing the prompt text.

  --output_file OUTPUT_FILE
                        Path to the file where the AI response will be saved.

  --model MODEL         Model used. Default is set in the config file.

  --system_message_file SYSTEM_MESSAGE_FILE
                        Path to the file containing the System message.

  --max_tokens MAX_TOKENS
                        Max tokens used in the api call. Default is set in the config file.

  --verbose VERBOSE     Verbose mode. Extra information will be printed to the console.  Good for debugging.
```
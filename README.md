
# AI-CLI
AI CLI is a commandline utility to batch process files through a openai model. You can process multiple files just loop over all the file paths and send the output to another path. You can also chain the output of one processed file to reimport into another cycle with a system prompt. Extreamely useful utility.

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

  --model {gpt-4,gpt-4-0314,gpt-4-32k,gpt-4-32k-0314,gpt-3.5-turbo,gpt-3.5-turbo-0301,text-davinci-003,code-davinci-002,text-davinci-001,text-curie-001,text-babbage-001,text-ada-001}  
                        Model used. Default is set in the config file.

  --system_message_file SYSTEM_MESSAGE_FILE
                        Path to the file containing the System message.

  --openai_api_key OPENAI_API_KEY
                        OpenAI api key. If passed it will ignore the one in the config      
                        file.

  --max_tokens MAX_TOKENS
                        Limits the number of tokens in the response. Default is set in the  
                        config file.

  --temperature TEMPERATURE
                        Controls randomness. Lower values make output more deterministic. 

  --top_p TOP_P         Controls diversity via nucleus sampling. 0.5 means half of all      
                        likelihood-weighted options are considered.

  --verbose {True,False}
                        Verbose mode. Extra information will be printed to the console.     
                        Good for debugging.

  --return_json {True,False}
                        Return JSON format of responses.

  --prompt_prepend_file PROMPT_PREPEND_FILE
                        Path to the file containing the prompt prepend text.
```


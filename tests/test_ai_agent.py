import unittest
from unittest.mock import patch, MagicMock
from colorama import Fore
from ai_agent import call_ai_agent

# tests/test_ai_agent.py


class TestCallAIAgentV2(unittest.TestCase):

    @patch("ai_agent.configparser.ConfigParser.get")
    @patch("ai_agent.openai.chat.completions.create")
    def test_missing_api_key(self, mock_openai_create, mock_config_get):
        # Simulate missing API key
        mock_config_get.side_effect = lambda section, key, fallback=None: None if key == "key" else fallback

        result = call_ai_agent("Test prompt")
        self.assertEqual(result, print(Fore.RED + "Error: API key not found in config.properties."))

    @patch("ai_agent.configparser.ConfigParser.get")
    @patch("ai_agent.openai.chat.completions.create")
    def test_successful_response_without_system_message(self, mock_openai_create, mock_config_get):
        # Mock configuration values
        mock_config_get.side_effect = lambda section, key, fallback=None: "test_key" if key == "key" else "gpt-3.5-turbo"

        # Mock OpenAI response
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content="Mocked response"))]
        mock_openai_create.return_value = mock_response

        result = call_ai_agent("Test prompt")
        self.assertEqual(result, "Mocked response")

    @patch("ai_agent.configparser.ConfigParser.get")
    @patch("ai_agent.openai.chat.completions.create")
    def test_successful_response_with_system_message(self, mock_openai_create, mock_config_get):
        # Mock configuration values
        mock_config_get.side_effect = lambda section, key, fallback=None: "test_key" if key == "key" else "gpt-3.5-turbo"

        # Mock OpenAI response
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content="Mocked response with system message"))]
        mock_openai_create.return_value = mock_response

        result = call_ai_agent("Test prompt", system_message="System message")
        self.assertEqual(result, "Mocked response with system message")

    @patch("ai_agent.configparser.ConfigParser.get")
    @patch("ai_agent.openai.chat.completions.create")
    def test_invalid_max_tokens(self, mock_openai_create, mock_config_get):
        # Mock configuration values
        mock_config_get.side_effect = lambda section, key, fallback=None: "test_key" if key == "key" else "invalid"

        result = call_ai_agent("Test prompt")
        self.assertEqual(result, print(Fore.RED + "Error calling AI agent: invalid literal for int() with base 10: 'invalid'"))

    @patch("ai_agent.configparser.ConfigParser.get")
    @patch("ai_agent.openai.chat.completions.create")
    def test_exception_handling(self, mock_openai_create, mock_config_get):
        # Mock configuration values
        mock_config_get.side_effect = lambda section, key, fallback=None: "test_key" if key == "key" else "gpt-3.5-turbo"

        # Simulate an exception in OpenAI API call
        mock_openai_create.side_effect = Exception("Mocked exception")

        result = call_ai_agent("Test prompt")
        self.assertEqual(result, print(Fore.RED + "Error calling AI agent: Mocked exception"))


if __name__ == "__main__":
        unittest.main()
    
import unittest
from unittest.mock import patch, MagicMock
from ai_agent import call_ai_agent

# File: tests/test_ai_agent.py



class TestCallAIAgent(unittest.TestCase):

    @patch("ai_agent.configparser.ConfigParser")
    def test_missing_api_key(self, mock_config):
        # Mock config to return no API key
        mock_config.return_value.get.return_value = None

        with self.assertLogs(level="ERROR") as log:
            response = call_ai_agent("Test prompt")
            self.assertIsNone(response)
            self.assertIn("Error: API key not found in config.properties.", log.output[0])

    @patch("ai_agent.openai.chat.completions.create")
    @patch("ai_agent.configparser.ConfigParser")
    def test_successful_response_without_system_message(self, mock_config, mock_openai):
        # Mock config to return API key and default model
        mock_config.return_value.get.side_effect = lambda section, key, fallback=None: {
            ("API", "key"): "test_api_key",
            ("CONFIG", "default_model"): "gpt-3.5-turbo",
            ("CONFIG", "max_tokens"): "100",
        }.get((section, key), fallback)

        # Mock OpenAI API response
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content="Test response"))]
        mock_openai.return_value = mock_response

        response = call_ai_agent("Test prompt")
        self.assertEqual(response, "Test response")

    @patch("ai_agent.openai.chat.completions.create")
    @patch("ai_agent.configparser.ConfigParser")
    def test_successful_response_with_system_message(self, mock_config, mock_openai):
        # Mock config to return API key and default model
        mock_config.return_value.get.side_effect = lambda section, key, fallback=None: {
            ("API", "key"): "test_api_key",
            ("CONFIG", "default_model"): "gpt-3.5-turbo",
            ("CONFIG", "max_tokens"): "100",
        }.get((section, key), fallback)

        # Mock OpenAI API response
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content="Test response with system message"))]
        mock_openai.return_value = mock_response

        response = call_ai_agent("Test prompt", system_message="System message")
        self.assertEqual(response, "Test response with system message")

    @patch("ai_agent.openai.chat.completions.create")
    @patch("ai_agent.configparser.ConfigParser")
    def test_exception_handling(self, mock_config, mock_openai):
        # Mock config to return API key and default model
        mock_config.return_value.get.side_effect = lambda section, key, fallback=None: {
            ("API", "key"): "test_api_key",
            ("CONFIG", "default_model"): "gpt-3.5-turbo",
            ("CONFIG", "max_tokens"): "100",
        }.get((section, key), fallback)

        # Mock OpenAI API to raise an exception
        mock_openai.side_effect = Exception("Test exception")

        with self.assertLogs(level="ERROR") as log:
            response = call_ai_agent("Test prompt")
            self.assertIsNone(response)
            self.assertIn("Error calling AI agent: Test exception", log.output[0])


if __name__ == "__main__":
    unittest.main()
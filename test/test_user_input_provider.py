# pylint: disable=missing-docstring
from unittest import TestCase, mock

import user_input_provider


class TestUserInputProvider(TestCase):
    @mock.patch("builtins.print")
    @mock.patch("builtins.input", create=True)
    def test_input_str(self, mock_input, mock_print):
        mock_input.side_effect = ["", " ", "Hello World!"]

        user_input = user_input_provider.input_str("Question")
        mock_print.assert_called_with("Your answer cannot be empty")
        mock_print.assert_called_with("Your answer cannot be empty")

        assert user_input == "Hello World!"

    @mock.patch("builtins.print")
    @mock.patch("builtins.input", create=True)
    def test_input_int(self, mock_input, mock_print):
        mock_input.side_effect = ["Hello World!", "-5", "-3.14159", "5"]

        user_input = user_input_provider.input_int("Question")
        mock_print.assert_called_with("Must be positive int")
        mock_print.assert_called_with("Must be positive int")
        mock_print.assert_called_with("Must be positive int")

        assert user_input == 5

    @mock.patch("builtins.print")
    @mock.patch("builtins.input", create=True)
    def test_input_float(self, mock_input, mock_print):
        mock_input.side_effect = ["Hello World!", "-3.14159"]

        user_input = user_input_provider.input_float("Question")
        mock_print.assert_called_with("Must be a float")

        assert user_input == -3.14159

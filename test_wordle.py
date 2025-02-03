"""
Wordle Test Case Suite
"""

import unittest
import sys
from unittest.mock import patch
import io
import os
import difflib
from wordle import (
    prepare_game,
    get_feedback,
    is_valid_guess,
    main,
    CORRECT_COLOR,
    WRONG_SPOT_COLOR,
    NOT_IN_WORD_COLOR,
    RESET_COLOR,
)


class TestGetFeedback(unittest.TestCase):
    """Get Feedback Tests"""

    def test_1(self):
        """get_feedback(): secret word basil and guessed word basil"""
        secret_word = "basil"
        guessed_word = "basil"
        actual = get_feedback(secret_word, guessed_word)
        expected = (
            f"{CORRECT_COLOR}b{RESET_COLOR}"
            f"{CORRECT_COLOR}a{RESET_COLOR}"
            f"{CORRECT_COLOR}s{RESET_COLOR}"
            f"{CORRECT_COLOR}i{RESET_COLOR}"
            f"{CORRECT_COLOR}l{RESET_COLOR}"
        )

        self.assertEqual(actual, expected)

    def test_2(self):
        """get_feedback(): secret word lever and guessed word light"""
        secret_word = "lever"
        guessed_word = "light"
        actual = get_feedback(secret_word, guessed_word)
        expected = (
            f"{CORRECT_COLOR}l{RESET_COLOR}"
            f"{NOT_IN_WORD_COLOR}i{RESET_COLOR}"
            f"{NOT_IN_WORD_COLOR}g{RESET_COLOR}"
            f"{NOT_IN_WORD_COLOR}h{RESET_COLOR}"
            f"{NOT_IN_WORD_COLOR}t{RESET_COLOR}"
        )

        self.assertEqual(actual, expected)

    def test_3(self):
        """get_feedback(): secret word llama and guessed word ladle"""
        secret_word = "llama"
        guessed_word = "ladle"
        actual = get_feedback(secret_word, guessed_word)
        expected = (
            f"{CORRECT_COLOR}l{RESET_COLOR}"
            f"{WRONG_SPOT_COLOR}a{RESET_COLOR}"
            f"{NOT_IN_WORD_COLOR}d{RESET_COLOR}"
            f"{WRONG_SPOT_COLOR}l{RESET_COLOR}"
            f"{NOT_IN_WORD_COLOR}e{RESET_COLOR}"
        )

        self.assertEqual(actual, expected)

    def test_4(self):
        """get_feedback(): secret word aback and guessed word abaca"""
        secret_word = "aback"
        guessed_word = "abaca"
        actual = get_feedback(secret_word, guessed_word)
        expected = (
            f"{CORRECT_COLOR}a{RESET_COLOR}"
            f"{CORRECT_COLOR}b{RESET_COLOR}"
            f"{CORRECT_COLOR}a{RESET_COLOR}"
            f"{CORRECT_COLOR}c{RESET_COLOR}"
            f"{NOT_IN_WORD_COLOR}a{RESET_COLOR}"
        )

        self.assertEqual(actual, expected)

    def test_5(self):
        """get_feedback(): secret word hello and guessed word label"""
        secret_word = "hello"
        guessed_word = "label"
        actual = get_feedback(secret_word, guessed_word)
        expected = (
            f"{WRONG_SPOT_COLOR}l{RESET_COLOR}"
            f"{NOT_IN_WORD_COLOR}a{RESET_COLOR}"
            f"{NOT_IN_WORD_COLOR}b{RESET_COLOR}"
            f"{WRONG_SPOT_COLOR}e{RESET_COLOR}"
            f"{WRONG_SPOT_COLOR}l{RESET_COLOR}"
        )

        self.assertEqual(actual, expected)

    def test_6(self):
        """get_feedback(): secret word gaily and guessed word hello"""
        secret_word = "gaily"
        guessed_word = "hello"
        actual = get_feedback(secret_word, guessed_word)
        expected = (
            f"{NOT_IN_WORD_COLOR}h{RESET_COLOR}"
            f"{NOT_IN_WORD_COLOR}e{RESET_COLOR}"
            f"{NOT_IN_WORD_COLOR}l{RESET_COLOR}"
            f"{CORRECT_COLOR}l{RESET_COLOR}"
            f"{NOT_IN_WORD_COLOR}o{RESET_COLOR}"
        )

        self.assertEqual(actual, expected)

    def test_7(self):
        """get_feedback(): secret word riped and guessed word crown"""
        secret_word = "riped"
        guessed_word = "crown"
        actual = get_feedback(secret_word, guessed_word)
        expected = (
            f"{NOT_IN_WORD_COLOR}c{RESET_COLOR}"
            f"{WRONG_SPOT_COLOR}r{RESET_COLOR}"
            f"{NOT_IN_WORD_COLOR}o{RESET_COLOR}"
            f"{NOT_IN_WORD_COLOR}w{RESET_COLOR}"
            f"{NOT_IN_WORD_COLOR}n{RESET_COLOR}"
        )

        self.assertEqual(actual, expected)

    def test_8(self):
        """get_feedback(): secret word table and guessed word metal"""
        secret_word = "table"
        guessed_word = "metal"
        actual = get_feedback(secret_word, guessed_word)
        expected = (
            f"{NOT_IN_WORD_COLOR}m{RESET_COLOR}"
            f"{WRONG_SPOT_COLOR}e{RESET_COLOR}"
            f"{WRONG_SPOT_COLOR}t{RESET_COLOR}"
            f"{WRONG_SPOT_COLOR}a{RESET_COLOR}"
            f"{WRONG_SPOT_COLOR}l{RESET_COLOR}"
        )

        self.assertEqual(actual, expected)

    def test_9(self):
        """get_feedback(): secret word table and guessed word metal"""
        secret_word = "index"
        guessed_word = "linen"
        actual = get_feedback(secret_word, guessed_word)
        expected = (
            f"{NOT_IN_WORD_COLOR}l{RESET_COLOR}"
            f"{WRONG_SPOT_COLOR}i{RESET_COLOR}"
            f"{WRONG_SPOT_COLOR}n{RESET_COLOR}"
            f"{CORRECT_COLOR}e{RESET_COLOR}"
            f"{NOT_IN_WORD_COLOR}n{RESET_COLOR}"
        )

        self.assertEqual(actual, expected)

    def test_10(self):
        """get_feedback(): secret word bleak and guessed word helix"""
        secret_word = "bleak"
        guessed_word = "helix"
        actual = get_feedback(secret_word, guessed_word)
        expected = (
            f"{NOT_IN_WORD_COLOR}h{RESET_COLOR}"
            f"{WRONG_SPOT_COLOR}e{RESET_COLOR}"
            f"{WRONG_SPOT_COLOR}l{RESET_COLOR}"
            f"{NOT_IN_WORD_COLOR}i{RESET_COLOR}"
            f"{NOT_IN_WORD_COLOR}x{RESET_COLOR}"
        )

        self.assertEqual(actual, expected)


class TestPrepareGame(unittest.TestCase):
    """Prepare Game Tests"""

    def test_1(self):
        """prepare_game(): 5 letter lowercase word"""
        sys.argv = ["wordle.py", "tests"]
        actual, _ = prepare_game()
        expected = "tests"
        self.assertEqual(actual, expected)

    def test_2(self):
        """prepare_game(): too many arguments"""
        sys.argv = ["wordle.py", "too", "many", "args"]
        with self.assertRaises(ValueError):
            prepare_game()

    def test_3(self):
        """prepare_game(): too many characters"""
        sys.argv = ["wordle.py", "toomanychars"]
        with self.assertRaises(ValueError):
            prepare_game()

    def test_4(self):
        """prepare_game(): invalid command line arguments"""
        sys.argv = ["wordle.py", "hello", "birdy", "again"]
        with self.assertRaises(ValueError):
            prepare_game()

    def test_5(self):
        """prepare_game(): bad user input"""
        sys.argv = ["wordle.py", "TESTS"]
        with self.assertRaises(ValueError):
            prepare_game()

    def test_6(self):
        """prepare_game(): seed"""
        sys.argv = ["wordle.py", "1234"]
        actual, _ = prepare_game()
        expected = "smell"
        self.assertEqual(actual, expected)

    def test_7(self):
        """prepare_game(): invalid command line argument"""
        sys.argv = ["wordle.py", "he110"]
        with self.assertRaises(ValueError):
            prepare_game()

    def test_8(self):
        """prepare_game(): bad user input"""
        sys.argv = ["wordle.py", "1."]
        with self.assertRaises(ValueError):
            prepare_game()

    def test_9(self):
        """prepare_game(): 5 letter lowercase word"""
        sys.argv = ["wordle.py", "hello"]
        actual, _ = prepare_game()
        expected = "hello"
        self.assertEqual(actual, expected)

    def test_10(self):
        """prepare_game(): seed"""
        sys.argv = ["wordle.py", "554"]
        actual, _ = prepare_game()
        expected = "trick"
        self.assertEqual(actual, expected)


class TestIsValidGuess(unittest.TestCase):
    """Is Valid Guess Tests"""

    def test_1(self):
        """is_valid_guess(): 5 letter lower case valid guess"""
        sys.argv = ["wordle.py", "table"]
        guess = "metal"
        _, valid_guesses = prepare_game()
        actual = is_valid_guess(guess, valid_guesses)
        expected = True
        self.assertEqual(actual, expected)

    def test_2(self):
        """is_valid_guess(): 5 letter lower case valid guess"""
        sys.argv = ["wordle.py", "154"]
        guess = "stars"
        _, valid_guesses = prepare_game()
        actual = is_valid_guess(guess, valid_guesses)
        expected = True
        self.assertEqual(actual, expected)

    def test_3(self):
        """is_valid_guess(): invalid guess due to @"""
        sys.argv = ["wordle.py", "elbow"]
        guess = "@llow"
        _, valid_guesses = prepare_game()
        actual = is_valid_guess(guess, valid_guesses)
        expected = False
        self.assertEqual(actual, expected)

    def test_4(self):
        """is_valid_guess(): 5 letter lower case valid guess"""
        sys.argv = ["wordle.py", "abaca"]
        guess = "gaily"
        _, valid_guesses = prepare_game()
        actual = is_valid_guess(guess, valid_guesses)
        expected = True
        self.assertEqual(actual, expected)

    def test_5(self):
        """is_valid_guess(): 5 letter lower case invalid guess (not a word)"""
        sys.argv = ["wordle.py", "hello"]
        guess = "djkaj"
        _, valid_guesses = prepare_game()
        actual = is_valid_guess(guess, valid_guesses)
        expected = False
        self.assertEqual(actual, expected)

    def test_6(self):
        """is_valid_guess(): 5 letter lower case invalid guess (nums)"""
        sys.argv = ["wordle.py", "hello"]
        guess = "1jkaj"
        _, valid_guesses = prepare_game()
        actual = is_valid_guess(guess, valid_guesses)
        expected = False
        self.assertEqual(actual, expected)

    def test_7(self):
        """is_valid_guess(): 5 letter invalid guess (casing)"""
        sys.argv = ["wordle.py", "train"]
        guess = "tRaIn"
        _, valid_guesses = prepare_game()
        actual = is_valid_guess(guess, valid_guesses)
        expected = False
        self.assertEqual(actual, expected)

    def test_8(self):
        """is_valid_guess(): invalid guess due to length and !"""
        sys.argv = ["wordle.py", "brain"]
        guess = "brains!"
        _, valid_guesses = prepare_game()
        actual = is_valid_guess(guess, valid_guesses)
        expected = False
        self.assertEqual(actual, expected)

    def test_9(self):
        """is_valid_guess(): 5 letter lower case valid guess"""
        sys.argv = ["wordle.py", "lllll"]
        guess = "prays"
        _, valid_guesses = prepare_game()
        actual = is_valid_guess(guess, valid_guesses)
        expected = True
        self.assertEqual(actual, expected)

    def test_10(self):
        """is_valid_guess(): 5 letter lower case valid guess with custom word"""
        sys.argv = ["wordle.py", "bleak"]
        guess = "adept"
        _, valid_guesses = prepare_game()
        actual = is_valid_guess(guess, valid_guesses)
        expected = True
        self.assertEqual(actual, expected)


class TestWordle(unittest.TestCase):
    """Functional Test Cases"""

    def check_diff(self, actual_output, output_file):
        """Helper function to check differences between actual output and expected output"""

        with open(
            os.path.join("expected_default_outputs", output_file), "r", encoding="UTF-8"
        ) as outfile:
            expected_default_output = outfile.read()

        with open(
            os.path.join("expected_high_contrast_outputs", output_file),
            "r",
            encoding="UTF-8",
        ) as outfile:
            expected_high_contrast_output = outfile.read()

        default_diff = list(
            difflib.unified_diff(
                expected_default_output.splitlines(keepends=True),
                actual_output.splitlines(keepends=True),
                fromfile="expected output",
                tofile="actual output",
                lineterm="",
            )
        )

        high_contrast_diff = list(
            difflib.unified_diff(
                expected_high_contrast_output.splitlines(keepends=True),
                actual_output.splitlines(keepends=True),
                fromfile="expected output",
                tofile="actual output",
                lineterm="",
            )
        )

        if len(default_diff) <= len(high_contrast_diff):
            diff_result = default_diff
        else:
            diff_result = high_contrast_diff

        if diff_result:
            diff_output = "\n".join(diff_result)
            self.fail(
                f"Differences found between actual output and {output_file}:\n{diff_output}"
            )

    def run_wordle_with_input(self, input_file):
        """Helper function to run wordle.py with input from a file and capture output as a string"""
        with open(input_file, "r", encoding="UTF-8") as infile:
            inputs = infile.read().splitlines()
        i = 0

        # Function to mock each input call
        def input_mock(prompt=""):
            nonlocal i
            # Print or log each input as it's read from the file
            if i < len(inputs):
                current_input = inputs[i]
                print(f"{prompt}{current_input}")
                i += 1
                return current_input
            raise EOFError("EOF when reading a line")

        output_buffer = io.StringIO()
        with patch("builtins.input", input_mock), patch(
            "sys.stdout", new=output_buffer
        ):
            sys.argv = ["wordle.py"]
            sys.argv.extend(input_file.split(".in")[0].split())
            main()

        return output_buffer.getvalue()

    def run_test_case(self, test_case):
        """Helper function to handle test case execution and diff checking"""
        input_file = f"{test_case}.in"
        output_file = f"{test_case}.ansi"

        actual_output = self.run_wordle_with_input(input_file)
        self.check_diff(actual_output, output_file)

    def test_154(self):
        """python3 wordle.py 154 < 154.in"""
        self.run_test_case("154")

    def test_999(self):
        """python3 wordle.py 999 < 999.in"""
        self.run_test_case("999")

    def test_basil(self):
        """python3 wordle.py basil < basil.in"""
        self.run_test_case("basil")

    def test_books(self):
        """python3 wordle.py books < books.in"""
        self.run_test_case("books")

    def test_brain(self):
        """python3 wordle.py brain < brain.in"""
        self.run_test_case("brain")

    def test_camel(self):
        """python3 wordle.py camel < camel.in"""
        self.run_test_case("camel")

    def test_great(self):
        """python3 wordle.py great < great.in"""
        self.run_test_case("great")

    def test_hatch(self):
        """python3 wordle.py Hatch < Hatch.in"""
        self.run_test_case("Hatch")

    def test_hello_birdy(self):
        """python3 wordle.py hello birdy"""
        self.run_test_case("hello birdy")

    def test_hello(self):
        """python3 wordle.py hello < hello.in"""
        self.run_test_case("hello")

    def test_kappa(self):
        """python3 wordle.py kappa < kappa.in"""
        self.run_test_case("kappa")

    def test_lllll(self):
        """python3 wordle.py lllll < lllll.in"""
        self.run_test_case("lllll")

    def test_mello(self):
        """python3 wordle.py mello < mello.in"""
        self.run_test_case("mello")

    def test_pivot(self):
        """python3 wordle.py pivot < pivot.in"""
        self.run_test_case("pivot")

    def test_right(self):
        """python3 wordle.py right < right.in"""
        self.run_test_case("right")

    def test_riped(self):
        """python3 wordle.py riped < riped.in"""
        self.run_test_case("riped")

    def test_sleep(self):
        """python3 wordle.py sleep < sleep.in"""
        self.run_test_case("sleep")

    def test_smoge(self):
        """python3 wordle.py smoge < smoge.in"""
        self.run_test_case("smoge")

    def test_table(self):
        """python3 wordle.py table < table.in"""
        self.run_test_case("table")

    def test_train(self):
        """python3 wordle.py train < train.in"""
        self.run_test_case("train")


if __name__ == "__main__":
    unittest.main()

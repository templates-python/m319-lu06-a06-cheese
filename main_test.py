import pytest
from main import main


def test_main_80(capsys, monkeypatch):
    """
    Test the main function with an input of 80 KD.
    """
    # Simulate user input
    monkeypatch.setattr('builtins.input', lambda _: "80")

    # Call the main function
    main()

    # Capture the output
    captured = capsys.readouterr()

    # Expected output
    expected_output = "75 KD\n1 KD\n1 KD\n1 KD\n1 KD\n1 KD\n"

    # Assert the output matches expected
    assert captured.out == expected_output


def test_main_26(capsys, monkeypatch):
    """
    Test the main function with an input of 26 KD.
    """
    # Simulate user input
    monkeypatch.setattr('builtins.input', lambda _: "26")

    # Call the main function
    main()

    # Capture the output
    captured = capsys.readouterr()

    # Expected output
    expected_output = "25 KD\n1 KD\n"

    # Assert the output matches expected
    assert captured.out == expected_output


def test_main_192(capsys, monkeypatch):
    """
    Test the main function with an input of 192 KD.
    """
    # Simulate user input
    monkeypatch.setattr('builtins.input', lambda _: "192")

    # Call the main function
    main()

    # Capture the output
    captured = capsys.readouterr()

    # Expected output for 192 KD
    expected_output = (
            "100 KD\n"
            "75 KD\n" +
            "1 KD\n" * 17  # 17 one-KD notes for the remaining 17 KD
    )

    # Assert the output matches expected
    assert captured.out == expected_output


def test_main_0(capsys, monkeypatch):
    """
    Test the main function with an input of 0 KD.
    """
    # Simulate user input
    monkeypatch.setattr('builtins.input', lambda _: "0")

    # Call the main function
    main()

    # Capture the output
    captured = capsys.readouterr()

    # Expected output (no bills for 0 KD)
    expected_output = ""

    # Assert the output matches expected
    assert captured.out == expected_output


def test_main_1(capsys, monkeypatch):
    """
    Test the main function with an input of 1 KD.
    """
    # Simulate user input
    monkeypatch.setattr('builtins.input', lambda _: "1")

    # Call the main function
    main()

    # Capture the output
    captured = capsys.readouterr()

    # Expected output
    expected_output = "1 KD\n"

    # Assert the output matches expected
    assert captured.out == expected_output


def test_main_300(capsys, monkeypatch):
    """
    Test the main function with an input of 300 KD.
    """
    # Simulate user input
    monkeypatch.setattr('builtins.input', lambda _: "300")

    # Call the main function
    main()

    # Capture the output
    captured = capsys.readouterr()

    # Expected output
    expected_output = "200 KD\n100 KD\n"

    # Assert the output matches expected
    assert captured.out == expected_output

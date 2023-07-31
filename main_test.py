import main

def test_lists(capsys):
    result = main.main()
    assert result.len() == 5

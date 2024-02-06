import lab1q7
from io import StringIO
from sys import stderr
def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('1000\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab1q7.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'{0.0}') != -1

def test_case2(monkeypatch, capsys):
    number_inputs = StringIO('5000\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab1q7.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'{250.0}') != -1

def test_case3(monkeypatch, capsys):
    number_inputs = StringIO('20000\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab1q7.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'{3000.0}') != -1

def test_case4(monkeypatch, capsys):
    number_inputs = StringIO('70000\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab1q7.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'{17500.0}') != -1
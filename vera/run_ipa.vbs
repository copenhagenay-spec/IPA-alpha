Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd /c """ & WScript.ScriptFullName & "\..\run_ipa.cmd""", 0, False

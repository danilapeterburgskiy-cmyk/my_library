[Setup]
AppName=My Library
AppVersion=1.0
DefaultDirName={autopf}\MyLibrary
DefaultGroupName=My Library
OutputDir=..\Output
OutputBaseFilename=MyLibrary_Setup
Compression=lzma

[Files]
Source: "..\dist\MyLibrary.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\My Library"; Filename: "{app}\MyLibrary.exe"
Name: "{autodesktop}\My Library"; Filename: "{app}\MyLibrary.exe"

[Run]
Filename: "{app}\MyLibrary.exe"; Description: "Запустить"; Flags: postinstall nowait
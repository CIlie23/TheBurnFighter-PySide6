powershell -Command "(Get-Content main.ui) -replace '<fontweight></fontweight>', '<bold>false</bold>' | Set-Content main.ui"
pyside6-uic main.ui -o modules/ui_main.py
pyside6-rcc resources.qrc -o resources_rc.py
python main.py
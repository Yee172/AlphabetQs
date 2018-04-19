python Main.py
If errorlevel 1
(
    python3 Main.py
    If errorlevel 1
    (
    	echo Could not find Python3
    )
)
Pause
exit

@echo off
REM Batch script for PowerShell users - avoids && command issues
echo Starting BrainVenture Academy...

echo Activating virtual environment...
call .\venv\Scripts\activate.bat

echo Installing/updating requirements...
pip install -r requirements.txt

echo Starting Streamlit application...
streamlit run app.py

echo.
echo Application started successfully!
echo Press Ctrl+C to stop the application.
pause

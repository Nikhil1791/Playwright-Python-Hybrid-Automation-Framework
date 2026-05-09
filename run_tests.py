@echo off

title Playwright Python Framework

echo ==========================================
echo PLAYWRIGHT PYTHON AUTOMATION FRAMEWORK
echo ==========================================

echo.

IF NOT EXIST reports (
    mkdir reports
)

IF NOT EXIST screenshots (
    mkdir screenshots
)

IF NOT EXIST logs (
    mkdir logs
)

echo Activating Virtual Environment...
call venv\Scripts\activate

echo.
echo Installing Dependencies...
pip install -r requirements.txt

echo.
echo Running Automation Tests...
pytest -v --html=reports/report.html --self-contained-html

echo.
echo ==========================================
echo EXECUTION COMPLETED
echo ==========================================

echo.
echo Opening HTML Report...

start reports\report.html

pause


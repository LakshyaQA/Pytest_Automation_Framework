@echo off
setlocal EnableDelayedExpansion

for /f "delims=" %%a in (pytest.file) do (
    echo %%a
    %%a
)

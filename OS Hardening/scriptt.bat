@echo off
set hardeningIndex=0
set totalPolicies=0
for /f "tokens=1,2,3 delims= " %%a in (sec.cfg) do (
    if %%a==MaximumPasswordAge if %%c==45 set /a hardeningIndex=hardeningIndex+1
    if %%a==MinimumPasswordAge if %%c==0 set /a hardeningIndex=hardeningIndex+1
    if %%a==PasswordHistorySize if %%c==0 set /a hardeningIndex=hardeningIndex+1
    set /a totalPolicies=totalPolicies+1
    echo %%a
)
echo Hardening Index of System is %hardeningIndex%




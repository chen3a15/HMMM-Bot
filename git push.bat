@echo off
git add .
set /p a="Ìá½»ÃèÊö£º"
git commit -m "%a%"
git push
pause
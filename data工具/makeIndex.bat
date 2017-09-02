@echo off
for /f "delims=" %%a in ('dir /b/a-d/oN *.jpg') do echo positive_samples/%%a  1 0 0 64 64>>pos.dat
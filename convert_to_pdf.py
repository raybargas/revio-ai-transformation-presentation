#!/usr/bin/env python3
import os
import subprocess
import sys

# HTML file path
html_file = "/Users/raybargas/Desktop/Presentations/The Future of Rev.io Product and Engineering.html"
pdf_file = "/Users/raybargas/Desktop/Rev.io AI Transformation.pdf"

# Create AppleScript to print to PDF using Safari
applescript = f'''
tell application "Safari"
    activate
    open POSIX file "{html_file}"
    delay 3
    
    tell application "System Events"
        keystroke "p" using command down
        delay 2
        click button "PDF" of sheet 1 of window 1 of process "Safari"
        delay 1
        click menu item "Save as PDF…" of menu 1 of button "PDF" of sheet 1 of window 1 of process "Safari"
        delay 2
        
        keystroke "Rev.io AI Transformation"
        delay 1
        
        keystroke "g" using {{command down, shift down}}
        delay 1
        keystroke "~/Desktop"
        delay 1
        keystroke return
        delay 1
        
        click button "Save" of sheet 1 of window 1 of process "Safari"
        delay 3
    end tell
    
    close window 1
end tell
'''

# Write AppleScript to temporary file
script_file = "/tmp/convert_to_pdf.applescript"
with open(script_file, 'w') as f:
    f.write(applescript)

# Execute AppleScript
subprocess.run(['osascript', script_file])

print(f"PDF should be saved to: {pdf_file}")
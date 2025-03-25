# ScreenChangeScript

# Automatic Screen Mode Switching Based on Power State

## Objective:
Develop a Python script that **automatically switches** the display mode between **"PC Screen Only"** and **"Extend Screen"** based on the **charging status** of a laptop or desktop. The script should run in the background without user intervention.

## Problem Description:
Users who work with **multiple monitors** often face situations where their external display setup is disrupted when **power is disconnected**. Manually changing display settings every time is inconvenient.

To solve this, the system should:
- **Detect power status changes** in real-time.
- **Automatically switch to "PC Screen Only"** when charging is disconnected.
- **Wait for 5 seconds and switch to "Extend Screen"** when charging is reconnected.
- **Run silently in the background** using Task Scheduler.

## Expected Outcome:
- The script will **seamlessly adjust** screen modes, enhancing productivity.
- Users will **not need to manually change display settings** each time power status changes.
- The program will run **automatically on startup** via Task Scheduler.

## How to Use:
1. Run the script manually or schedule it via Task Scheduler.
2. The script will detect charging status and adjust screen mode accordingly.

---

## 🔧 Setup Guide: Running the Script Automatically

### **Step 1: Create a Batch File**
1. Open **Notepad** and paste the following code:

   ```batch
   @echo off
   pythonw "C:\path\to\your\script\screen_switch.py"

2. Replace C:\path\to\your\script\screen_switch.py with the actual path to your Python script.

3. Click File → Save As.

4. Choose "All Files" as file type.

5. Name it screen_switch.bat.

6. Save it in a location like C:\scripts\.


### **Step 2: Add to Task Scheduler**
1. Open Task Scheduler (Win + R → Type taskschd.msc → Press Enter).

2. Click "Create Basic Task" (Right panel).

3. Name it "Screen Switch Automation".

4. Click Next, select "When the computer starts", and click Next.

5. Choose "Start a Program" and click Next.

6. Browse and select the screen_switch.bat file.

7. Click Finish.

### **Step 3: Verify the Task**
  - Restart your PC and check if the script runs automatically.  
    OR
  - If it doesn't, open Task Scheduler, find the task, right-click, and select Run to test it.

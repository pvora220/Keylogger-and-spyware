# Key Logger

## Overview

This repository contains a Python-based academic prototype developed for study and demonstration purposes in a controlled environment. The code explores low-level input monitoring techniques, periodic data collection, and multiple reporting approaches as part of a security-focused software project.

The current codebase includes experiments around:

- keyboard event capture
- local text logging
- periodic screenshot collection
- basic audio recording
- timed background reporting
- outbound delivery through email and webhook-based workflows

## Academic Context

This project should be treated as a research artifact for supervised coursework, malware analysis, and defensive security discussion. It is not intended for real-world deployment, covert monitoring, unauthorized data collection, or use on systems without the explicit knowledge and permission of all participants.

## Repository Structure

The repository appears to contain multiple iterations of the same idea, including standalone scripts and a subfolder with expanded experiments.

- `01/`: main project variant with Python scripts, requirements, screenshots, and sample outputs
- `keywebhook.py`: webhook-based logging and screenshot reporting experiment
- `keyobfus.py`, `keyhook obfus.py`: obfuscated or alternate variants
- `key with ss.py`, `key with ss and log.py`: versions combining keystroke capture with screenshots
- `keyss.py`: alternate screenshot/logging script
- `antikey.py`: related experimental file
- `data.txt`, `keystrokes.txt`, `keylogger.txt`: sample local output/log files
- `virus total/`: images related to external scan or analysis results

## Technologies Observed

Based on the source files, the project uses or references:

- Python
- `pynput` for keyboard input hooks
- `pyscreenshot` or `PIL.ImageGrab` for screenshots
- `sounddevice` and `wave` for audio capture
- `requests` for webhook communication
- `smtplib` and email MIME helpers for mail-based reporting
- `threading` and timers for background execution

The `01/requirements.txt` file currently lists:

- `pynput==1.7.3`
- `pyscreenshot==0.5.1`
- `sounddevice==0.4.3`
- `Pillow==9.3.0`

## Notes on the Current Implementation

From inspection of the code, the repository contains several experimental implementations rather than a single polished application. Different files demonstrate different transport and collection methods, and some scripts appear to include placeholder credentials, hardcoded endpoints, or proof-of-concept logic intended for testing.

The codebase also mixes logging, capture, background threads, and cleanup behavior in ways that suggest an exploratory final project rather than a production-ready system.

## Ethics and Safety

Input monitoring software is highly sensitive. Even in academic settings, any testing should be limited to:

- personally owned devices or isolated lab environments
- explicit written consent from all participants
- local demonstrations supervised by an instructor
- defensive research, detection engineering, or controlled proof-of-concept work

This repository should not be used to capture credentials, monitor third parties, evade detection, or collect data without informed permission.

## Disclaimer

This README documents the repository as it currently exists for academic description only. Anyone reviewing or extending this project should prioritize consent, legality, and defensive security principles before making further changes.

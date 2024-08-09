# WhatsApp Automation Scripts

This repository contains two Python scripts that automate tasks on WhatsApp using Selenium. These scripts are useful for managing WhatsApp groups and sending messages in bulk.

## Table of Contents
- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Scripts](#scripts)
  - [1. Add Members to WhatsApp Group](#1-add-members-to-whatsapp-group)
  - [2. Send Individual WhatsApp Messages](#2-send-individual-whatsapp-messages)
- [Usage](#usage)
  - [Running the Scripts](#running-the-scripts)
- [File Structure](#file-structure)

## Project Overview

During the organization of an event, participants were required to fill out a Google form, and upon submission, they were expected to join a WhatsApp group via a link. However, the link was not provided, making it difficult to manually share it with over 130 participants. To solve this, two Python scripts were developed:

1. **Add Members to a WhatsApp Group**: This script reads a list of phone numbers from a CSV file and adds them to a pre-existing WhatsApp group.
2. **Send Individual WhatsApp Messages**: This script reads phone numbers from a CSV file and sends personalized messages to each number individually.

## Prerequisites

Ensure you have the following installed on your machine:

- Python 3.x
- Google Chrome browser
- ChromeDriver (automatically handled by `webdriver_manager`)
- Pandas library
- Selenium library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ayuktha63/whatsapp-scripts.git
   cd whatsapp-automation
    ```
2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Running the Scripts
    Add Members to WhatsApp Group:

    Ensure you have the list of phone numbers in a phone_number.csv file.
    Run the script group_add_members.py using the command:
    ```bash
    python group_add_members.py
    ```
    Send Individual WhatsApp Messages:
    Ensure you have the list of phone numbers in a phone_number.csv file.

    Run the script individual_message_sender.py using the command:
    ```bash
    python individual_message_sender.py
    ```
4. File Structure
    ```bash
    /
    .
    ├── Readme.md
    ├── group_add_members.py                # Script to add members to a WhatsApp group
    ├── individual_message_sender.py        # Script to send individual WhatsApp messages
    ├── phone_number.csv                    # CSV file with phone numbers
    └── requirements.txt                    # List of required Python packages
    ```

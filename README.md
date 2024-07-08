# Gym Membership Management System

## Overview

This project is a command-line interface (CLI) application for managing gym memberships. It allows users to create, read, update, and delete gyms and members. The project uses Python and SQLite to handle the database operations.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Project Structure](#project-structure)
- [Models](#models)
- [CLI](#cli)
- [Helper Functions](#helper-functions)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Cloning the Repository

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/gym-membership-management.git
    cd gym-membership-management
    ```

### Setting Up the Virtual Environment

#### On Windows

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    venv\Scripts\activate

### Installing Dependencies

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**
    ```bash
    python lib/cli.py
    ```

2. **Main Menu Options:**
    - `G`: Access the gyms menu.
    - `E`: Exit the application.

## Features

- **Manage Gyms:**
  - Add new gyms.
  - View details of existing gyms.
  - Delete gyms.

- **Manage Members:**
  - Add new members to a gym.
  - View details of existing members.
  - Delete members.

- **Data Persistence:**
  - All data is stored in an SQLite database (`gym_database.db`).

## Project Structure

gym-membership-management/
│
├── lib/
│ ├── cli.py # Main CLI application
│ └── helpers.py # Helper functions for CLI operations
│
├── models/
│ ├── init.py # Database initialization and table creation
│ └── model_1.py # Member and Gym models
│
├── gym_database.db # SQLite database file
├── requirements.txt # Python dependencies
└── README.md # Project README file

## Models

### Member

Represents a gym member with attributes:
- `first_name`
- `last_name`
- `age`
- `gender`
- `membership_type`
- `gym_id`

Methods:
- `save()`: Saves the member to the database.
- `delete()`: Deletes the member from the database.
- `get_all()`: Retrieves all members.
- `find_by_id(member_id)`: Finds a member by their ID.
- `find_members_by_gym(gym_id)`: Finds all members of a specific gym.
- `delete_by_id(member_id)`: Deletes a member by their ID.

### Gym

Represents a gym with attributes:
- `name`
- `location`
- `opening_hours`
- `closing_hours`

Methods:
- `save()`: Saves the gym to the database.
- `delete()`: Deletes the gym from the database.
- `get_all()`: Retrieves all gyms.
- `find_by_id(gym_id)`: Finds a gym by its ID.
- `delete_by_id(gym_id)`: Deletes a gym by its ID.

## CLI

The CLI application provides a user-friendly interface to manage gyms and members. It includes menus for various operations and ensures proper input validation.

### Main Menu

- `G`: Access the gyms menu.
- `E`: Exit the program.

### Gyms Menu

- `A`: Add a new gym.
- `E`: Exit the program.
- Select a gym number to view its details and manage its members.

### Members Menu

- `A`: Add a new member to the selected gym.
- `D`: Delete the selected gym.
- Select a member number to view their details and delete them.

## Helper Functions

The helper functions in `helpers.py` handle various operations like:
- Exiting the program.
- Signing up new members and gyms.
- Finding members and gyms by ID.
- Deleting members and gyms by ID.



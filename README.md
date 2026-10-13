# Quiz Game — General Algorithm and OOP Design

## Project Overview

Build a quiz game that presents questions to a player, checks their answers, updates and displays their score progressively, and records completed games in a persistent JSON leaderboard.

The game retrieves a pool of 100 questions from an API and randomly selects 12 distinct questions for each game session.

## Main Menu

When the application starts, display these options:

1. Play Game
2. Check Leaderboard
3. Quit

Keep displaying the menu until the user chooses **Quit**.

---

## General Algorithm

### Phase 1: Initialise the Application

```text
BEGIN

    Load leaderboard records from the JSON file

    IF the JSON file does not exist
        Initialise an empty leaderboard
    END IF

    REPEAT

        Display the main menu:
            1. Play Game
            2. Check Leaderboard
            3. Quit

        Receive the user's menu choice
```

### Phase 2: Play Game

```text
        IF the user's choice is 1 THEN

            Ask the player to enter their name

            Create a Player object using the player's name

            Retrieve the available questions from the API

            IF the questions cannot be retrieved
                Display an error message
                Return to the main menu
            END IF

            Validate the question data

            IF fewer than 12 valid questions are available
                Display an insufficient-questions message
                Return to the main menu
            END IF

            Randomly select 12 distinct questions

            Create a Question object for each selected question

            Create a QuizBrain object using the 12 Question objects

            Initialise the QuizBrain score to zero

            Initialise the current question position
```

### Phase 3: Run the Quiz

```text
            WHILE questions remain

                Retrieve the current question

                Display the question to the player

                Receive the player's answer

                Check the player's answer against the correct answer

                IF the answer is correct THEN
                    Increase the QuizBrain score
                    Display a correct-answer message
                ELSE
                    Display an incorrect-answer message
                END IF

                Display the current QuizBrain score

                Update the question position

            END WHILE
```

### Phase 4: Complete the Game and Save the Result

```text
            Retrieve the final score from QuizBrain

            Transfer the final score to the Player object

            Display the player's name

            Display the final score

            Display the total number of questions answered

            Load the existing leaderboard records from the JSON file

            Create a completed-game record containing:
                Player name
                Final score

            Add the completed-game record to the leaderboard

            Sort the leaderboard by score in descending order

            Save the updated leaderboard to the JSON file

            Display a game-completion message
```

### Phase 5: Check the Leaderboard

```text
        ELSE IF the user's choice is 2 THEN

            Load leaderboard records from the JSON file

            IF the leaderboard contains no records
                Display a message that the leaderboard is empty
            ELSE
                Sort the records by score in descending order

                Display the ranked leaderboard containing:
                    Position
                    Player name
                    Score
            END IF
```

### Phase 6: Quit or Handle an Invalid Choice

```text
        ELSE IF the user's choice is 3 THEN

            Display an exit message

        ELSE

            Display an invalid-choice message

        END IF

    UNTIL the user's choice is 3

END
```

---

## Proposed Project Structure

```text
quiz_project/
│
├── main.py
├── question_model.py
├── player.py
├── quiz_brain.py
├── data.py
├── leaderboard.py
└── leaderboard.json
```

## Module and Class Responsibilities

### `main.py` — Main Program

Responsible for coordinating the overall application.

- Display and process the main menu.
- Ask for the player's name before the game begins.
- Request questions through the data module.
- Randomly select 12 distinct questions.
- Create the necessary objects.
- Run the main game loop.
- Display the final result.
- Coordinate leaderboard operations.
- Return to the menu after a game or leaderboard view.
- Exit when the user chooses Quit.

### `question_model.py` — `Question` Class

Represents one quiz question.

**Attributes:**

- Question text.
- Correct answer.

Each selected question is represented by its own `Question` object.

### `player.py` — `Player` Class

Represents the person playing the game.

**Attributes:**

- Player name.
- Player score, initially zero or unset until the game is completed.

The player's score is updated only when the quiz ends. During gameplay, `QuizBrain` keeps track of the live score. At the end, the final quiz score is transferred to the `Player` object.

For this design, the player's score represents the result of the current completed game, not a cumulative total across all games.

### `quiz_brain.py` — `QuizBrain` Class

Manages the quiz session.

Responsibilities:

- Store or receive the selected question objects.
- Track the current question position.
- Determine whether questions remain.
- Provide the current question.
- Check the player's answer.
- Increase the live score when an answer is correct.
- Make the current score available to the main program.
- Track progress until all questions have been answered.

`QuizBrain` owns the live score during gameplay. The `Player` object's score is updated only after the quiz finishes.

### `data.py` — Question Data and API

Responsible for retrieving question data from the external API.

- Make the API request.
- Handle request failures.
- Extract the question data from the response.
- Validate that the returned data is usable.
- Provide the question data to `main.py`.

Keep API retrieval separate from gameplay logic so each part has a clear responsibility.

### `leaderboard.py` — Leaderboard Operations

Responsible for managing saved game results.

- Load records from the JSON file.
- Handle a missing or empty file.
- Add a completed-game record.
- Sort records by score in descending order.
- Display the ranked leaderboard.
- Save updated records to the JSON file.

A leaderboard module does not automatically need a `Leaderboard` class. Ordinary functions may be sufficient unless a class provides a useful way to represent and manage leaderboard state.

### `leaderboard.json` — Persistent Storage

Stores completed-game records so they remain available after the application closes.

Each record should contain at least:

- Player name.
- Final score.

Each completed game is stored as a separate record, so one player can appear more than once if they play multiple games.

---

## How the Components Work Together

1. `main.py` displays the menu.
2. If the player chooses **Play Game**, the program asks for their name and creates a `Player` object.
3. `main.py` asks `data.py` to retrieve the questions.
4. The program validates the returned data and randomly selects 12 distinct questions.
5. Each selected question is represented by a `Question` object.
6. `main.py` passes the selected question objects to `QuizBrain`.
7. The main loop coordinates each turn while `QuizBrain` manages question progression, answer checking and the live score.
8. When the quiz ends, `main.py` transfers the final score to the `Player` object.
9. `leaderboard.py` records the player's name and final score in `leaderboard.json`.
10. If the player chooses **Check Leaderboard**, the program loads and displays saved records.
11. If the player chooses **Quit**, the application exits.

---

## Important Design Rules

1. **Separate responsibilities.** Each class or module should have a clear purpose.
2. **A module is not a class.** Modules organise code into files; classes model objects with related data and behaviour.
3. **`Question` represents one question.** It stores the question text and correct answer together.
4. **`QuizBrain` manages the active quiz.** It tracks progress, checks answers and maintains the live score.
5. **`Player` represents the player.** It stores the player's name and receives the final score when the game ends.
6. **`main.py` coordinates the application.** It should not contain every detail of API access, quiz management and file handling.
7. **Validate external data.** Handle API failures, malformed questions and fewer than 12 valid questions.
8. **Persist completed games.** Save results to JSON so the leaderboard survives application restarts.
9. **Handle an empty leaderboard.** The application should work when the JSON file does not exist or contains no records.
10. **Define tie handling when implementing ranking.** Scores should be sorted in descending order, and the chosen approach for equal scores should be consistent.

---

## Recommended Implementation Order

Develop and test the project in small stages:

1. Write the algorithm for the `Question` class.
2. Write the algorithm for the `Player` class.
3. Write the algorithm for `QuizBrain`.
4. Design the API retrieval and validation functions in `data.py`.
5. Design the leaderboard loading, saving, sorting and display operations.
6. Write the detailed `main.py` algorithm for the menu and game loop.
7. Implement each algorithm in Python.
8. Test correct and incorrect answers, score updates, API failures, missing JSON files, leaderboard ranking and quitting.

**Goal:** Use this document as a blueprint. Develop each class and module's detailed algorithm before writing its Python implementation, so the final program is built from your own reasoning rather than by following a tutorial line by line.

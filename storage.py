"""A place to store results"""

import sqlite3
from pathlib import Path


class SQLiteStorage:
    def __init__(self, file_location: Path):
        self.connection = sqlite3.connect(file_location)
        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Classes (
                ClassID int NOT NULL,
                ClassName varchar(255) NOT NULL,
                PRIMARY KEY (ClassID)
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Pupils (
                PupilID int NOT NULL,
                Name varchar(255) NOT NULL,
                ClassID int NOT NULL,
                PRIMARY KEY (PupilID),
                FOREIGN KEY (ClassID) REFERENCES Classes(ClassID)
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Scores (
                PupilID int NOT NULL,
                Score int NOT NULL,
                PRIMARY KEY (PupilID),
                FOREIGN KEY (PupilID) REFERENCES Pupils(PupilID)
            )
            """
        )

    # def add_score(self, name: str, score: int, class_id: int):
    #   """Adds the user's score to the DB, with the score being a percentage"""
    #    cursor = self.connection.cursor()

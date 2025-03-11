"""A place to store results"""

import sqlite3
import uuid
from pathlib import Path

from pupil import Pupil
from school_class import SchoolClass


class SQLiteStorage:
    """A place to store results"""

    def __init__(self, file_location: Path):
        self.connection = sqlite3.connect(file_location)
        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Classes (
                ClassID varchar(255) NOT NULL,
                ClassName varchar(255) NOT NULL,
                PRIMARY KEY (ClassID)
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Pupils (
                PupilID varchar(255) NOT NULL,
                Name varchar(255) NOT NULL,
                ClassID varchar(255) NOT NULL,
                PRIMARY KEY (PupilID),
                FOREIGN KEY (ClassID) REFERENCES Classes(ClassID)
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Scores (
                PupilID varchar(255) NOT NULL,
                Score int NOT NULL,
                Date DATE NOT NULL,
                PRIMARY KEY (PupilID),
                FOREIGN KEY (PupilID) REFERENCES Pupils(PupilID)
            )
            """
        )

    def add_score(self, pupil: Pupil, score: int, school_class: SchoolClass):
        """Adds the user's score to the DB, with the score being a percentage"""
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO Scores VALUES(?, ?, ?)",
            (pupil.pupil_id, score, school_class.school_class_id),
        )
        self.connection.commit()

    def add_pupil(self, name: str, school_class: SchoolClass) -> Pupil:
        """Adds a pupil to the database and returns their Pupil object"""
        cursor = self.connection.cursor()
        pupil_uuid: uuid.UUID = uuid.uuid4()
        cursor.execute(
            "INSERT INTO Pupils VALUES(?, ?, ?)",
            (str(pupil_uuid), name, school_class.school_class_id),
        )
        self.connection.commit()
        return Pupil(name, pupil_uuid)

    def add_school_class(self, name: str) -> SchoolClass:
        """Adds a school class to the database and returns it's type"""
        cursor = self.connection.cursor()
        school_class_uuid: uuid.UUID = uuid.uuid4()
        cursor.execute(
            "INSERT INTO Classes VALUES(?, ?)", (str(school_class_uuid), name)
        )
        self.connection.commit()
        return SchoolClass(name, school_class_uuid)

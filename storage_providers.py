"""A place to store results"""

import pathlib
import sqlite3
import uuid
from pathlib import Path

from pupil import Pupil
from school_class import SchoolClass
import user_input_provider


class _SQLiteStorage:
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

    def add_score(self, pupil: Pupil, score_percent: int, school_class: SchoolClass):
        """Adds the user's score to the DB, with the score being a percentage"""
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO Scores VALUES(?, ?, ?)",
            (pupil.pupil_id, score_percent, school_class.school_class_id),
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
        return Pupil(name, pupil_uuid, school_class.school_class_id)

    def add_school_class(self, name: str) -> SchoolClass:
        """Adds a school class to the database and returns it's type"""
        cursor = self.connection.cursor()
        school_class_uuid: uuid.UUID = uuid.uuid4()
        cursor.execute(
            "INSERT INTO Classes VALUES(?, ?)", (str(school_class_uuid), name)
        )
        self.connection.commit()
        return SchoolClass(name, school_class_uuid)
    
    def get_school_class_by_uuid(self, class_id: uuid.UUID) -> SchoolClass:
        """Gets a SchoolClass from a UUID"""
        cursor = self.connection.cursor()
        response = cursor.execute("SELECT ClassID, ClassName FROM Classes WHERE ClassID=?", (str(class_id))).fetchone()
        if response == None:
            raise Exception("No School Class with UUID: " + str(class_id))
        
        return SchoolClass(response[1], response[0])
    
    def remove_school_class_by_uuid(self, class_id: uuid.UUID) -> None:
        """Removes a school class"""
        cursor = self.connection.cursor()

        cursor.execute("DELETE FROM Classes WHERE ClassID=?", (class_id))
        self.connection.commit()
    
    def rename_school_class_by_uuid(self, class_id: uuid.UUID, new_name: str) -> None:
        """Renames a school class, keeping the uuid the same"""
        cursor = self.connection.cursor()

        cursor.execute("UPDATE Classes SET ClassName = ? WHERE ClassID = ?", (new_name, str(class_id)))
        self.connection.commit()

    
    def select_pupil(self) -> Pupil:
        """An interactive method that will prompt the user to select a pupil, recurs infinitely until the user has selected one"""
        cursor = self.connection.cursor()

        # Repeat looking for pupils until one is found
        while True:
            searching_name = user_input_provider.input_str("pupil name: ")

            response = cursor.execute("SELECT Name, PupilID, ClassID FROM Pupils WHERE Name=?", (searching_name)).fetchall()
            if len(response) == 0:
                print("No pupils found with that name")
            if len(response) == 1:
                correct_response = response[0]
                return Pupil(correct_response[0], correct_response[1], correct_response[2])

            if len(response) > 1:
                print(f"There is more than one pupil with the name {searching_name}")
                looking_at_pupils: list[Pupil] = []
                for current_response in response:
                    looking_at_pupils.append(Pupil(current_response[0], current_response[1], current_response[2]))
                
                user_selected_pupil_id: int =  user_input_provider.ask_menu("Select Pupil", looking_at_pupils)
                return looking_at_pupils[user_selected_pupil_id]
    
    def select_school_class(self) -> SchoolClass:
        cursor = self.connection.cursor()

        responses = cursor.execute("SELECT ClassID, ClassName FROM Classes").fetchall()
        all_school_classes: list[SchoolClass] = []

        for response in responses:
            all_school_classes.append(SchoolClass(response[1], response[0]))
        
        selected_school_class_id = user_input_provider.ask_menu("Select a school class", all_school_classes)
        return all_school_classes[selected_school_class_id]

# This class should be a singleton. This provides an easy way to access it everywhere
storage_instance = _SQLiteStorage(pathlib.Path(__file__).parent.resolve() / "database.db")
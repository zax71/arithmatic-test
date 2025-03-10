import uuid
from dataclasses import dataclass


@dataclass
class Pupil:
    """A pupil in the database"""

    name: str
    pupil_id: uuid.UUID

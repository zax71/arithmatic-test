import uuid
from dataclasses import dataclass


@dataclass
class SchoolClass:
    """A pupil in the database"""

    class_name: str
    school_class_id: uuid.UUID

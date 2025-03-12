import uuid
from dataclasses import dataclass


@dataclass
class Pupil:
    """A pupil in the database"""

    name: str
    pupil_id: uuid.UUID
    school_class_id: uuid.UUID

    def __str__(self) -> str:
        # Local import to avoid circular import
        from storage_providers import storage_instance
        return self.name + " in " + storage_instance.get_school_class_by_uuid(self.school_class_id).class_name

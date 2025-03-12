from storage_providers import storage_instance
import user_input_provider
from pupil import Pupil
from school_class import SchoolClass

  
def main_menu():
  match user_input_provider.ask_menu("Pupil Editor", ["Add pupil", "Remove pupil", "Rename pupil"]):
    case 1:
      _add_pupil()
    case 2:
      _remove_pupil()
    case 3:
      _rename_pupil()
  
def _add_pupil():
  name: str = user_input_provider.input_str("What us the pupil's name: ")
  school_class: SchoolClass = storage_instance.select_school_class()

  storage_instance.add_pupil(name, school_class)

def _remove_pupil():
  selected_pupil: Pupil = storage_instance.select_pupil()
  storage_instance.remove_pupil(selected_pupil)

def _rename_pupil():
  selected_pupil: Pupil = storage_instance.select_pupil()
  new_name: str = user_input_provider.input_str("New name of pupil: ")
  storage_instance.rename_pupil(selected_pupil, new_name)

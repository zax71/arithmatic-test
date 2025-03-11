from storage_providers import storage_instance
import user_input_provider
from pupil import Pupil

  
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

  # TODO: Implement adding pupil
  storage_instance.add_pupil()

def _remove_pupil():
  ...

def _rename_pupil():
  ...

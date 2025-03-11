import user_input_provider
from storage_providers import storage_instance
from school_class import SchoolClass

def main_menu():
    match user_input_provider.ask_menu("School Class Editor", ["Add class", "Remove class", "Rename class"]):
        case 1:
            _add_class()
        case 2:
            _remove_class()
        case 3:
            _rename_class()
  

def _add_class():
    new_school_class_name = user_input_provider.input_str("Name of class: ")
    storage_instance.add_school_class(new_school_class_name)

def _remove_class():
    selected_school_class: SchoolClass = storage_instance.select_school_class()
    storage_instance.remove_school_class_by_uuid(selected_school_class.school_class_id)

def _rename_class():
    selected_school_class: SchoolClass = storage_instance.select_school_class()
    new_school_class_name: str = user_input_provider.input_str("New name: ")
    storage_instance.rename_school_class_by_uuid(selected_school_class, new_school_class_name)

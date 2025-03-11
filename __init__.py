"""Gives the user a set of arithmetic questions"""

import pathlib
import random
import ui


import ui.main_game_manager
import ui.pupil_editor_manager
import ui.school_class_editor_manager
import user_input_provider
from storage_providers import storage_instance

def main():
    """The main function, the entrypoint"""

    menu_response = user_input_provider.ask_menu("Main Menu", ["Run game", "Open pupil editor", "Open class editor", "Generate report"])

    match menu_response:
        case 1:
            ui.main_game_manager.start_game()
        case 2:
            ui.pupil_editor_manager.main_menu()
        case 3:
            ui.school_class_editor_manager.main_menu()
        case 4:
            ...
    

    ## Finally, clean up
    storage_instance.connection.close()

    




if __name__ == "__main__":
    main()

from app import EngineeringFileManagerApp
from application_state import ApplicationState

if __name__ == "__main__":

    state = ApplicationState()

    app = EngineeringFileManagerApp(state)

    app.run()
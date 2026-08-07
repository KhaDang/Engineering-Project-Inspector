class ApplicationState:

    def __init__(self):

        self._observers = []

        self.comparison_results = []

        self.current_tab = None

        self.theme = "flatly"

        self.project_path = None

    def add_observer(self, observer):

        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)
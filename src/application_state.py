class ApplicationState:

    def __init__(self):

        self._observers = []

        self.comparison_results = []

        self.current_tab = None

        self.comparison_completed: bool = False

        self.theme = "flatly"

        self.project_path = None

    def add_observer(self, observer):

        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify(self):

        for observer in self._observers:
            observer.update(self)

    def set_comparison_results(self, results):
        self.comparison_results = results
        self.comparison_completed = True
        self.notify()

    def set_current_tab(self, tab_name):

        if self.current_tab == tab_name:
            return

        self.current_tab = tab_name

        self.notify()

        print(f"Observer get notified the current tab is: {self.current_tab}")
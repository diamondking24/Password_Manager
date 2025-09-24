from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical, ScrollableContainer
from textual.widgets import (
    Header, Footer, Button, Input, DataTable, Static, 
    TextArea, Checkbox, ProgressBar, Label
)
from textual.screen import Screen
from textual import events

class PasswordEntry:
    '''A class to represent a password entry'''
    def __init__(self, username: str, password: str, url: str, notes: str):
        self.username = username
        self.password = password
        self.url = url
        self.notes = notes

class Atlas(App):
    '''The Atlas application'''
    def __init__(self):
        super().__init__()
        self.passwords_entries = []

    

    CSS_PATH = "styles.css" #Path to the CSS file
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    
    def compose(self) -> ComposeResult:
        ''' Creates child widgets for the app'''
        yield Header(id="Header", classes="header", show_clock=True) #Header widget at the top of the app
        with Container(id="main-container"):
            with Horizontal(id="top-section", classes="Horizontal"):
                with Vertical(id="left-panel"):
                    yield Button("Add Entry", id="add-entry-btn")
                    yield Button("Delete Entry", id="delete-entry-btn")
                    yield Button("Export", id="export-btn")
                    yield Button("Import", id="import-btn")
                with Vertical(id="right-panel"):
                    yield DataTable(id="password-table")
            with Horizontal(id="bottom-section"):
                with Vertical(id="entry-details"):
                    yield Input(placeholder="Username", id="username-input")
                    yield Input(placeholder="Password", id="password-input")
                    yield Input(placeholder="URL", id="url-input") 
                with Vertical(id="actions-panel"):
                    yield Button("Save", id="save-btn")
                    yield Button("Cancel", id="cancel-btn")
                    
        yield Footer(id="Footer", classes="footer") #Footer widget at the bottom of the app


    def action__toggle_dark(self) -> None:
        '''An action to toggle dark mode'''
        self.theme = ("dark" if self.theme == "light" else "light")   



if __name__ == "__main__":
    app = Atlas()
    app.run()


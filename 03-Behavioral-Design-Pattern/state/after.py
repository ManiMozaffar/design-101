from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def next(self, document: "Document"):
        pass

    @abstractmethod
    def reject(self, document: "Document"):
        pass


class DraftState(State):
    def next(self, document: "Document"):
        document.state = ModerationState()
        print("Document sent for moderation.")

    def reject(self, document: "Document"):
        document.state = RejectedState()
        print("Document rejected.")


class ModerationState(State):
    def next(self, document: "Document"):
        document.state = PublishedState()
        print("Document published.")

    def reject(self, document: "Document"):
        document.state = RejectedState()
        print("Document rejected.")


class PublishedState(State):
    def next(self, document: "Document"):
        print("Document is already published.")

    def reject(self, document: "Document"):
        print("Cannot reject a published document.")


class RejectedState(State):
    def next(self, document: "Document"):
        print("Rejected document cannot change state.")

    def reject(self, document: "Document"):
        print("Document is already rejected.")


class Document:
    def __init__(self):
        self.state: State = DraftState()

    def next(self):
        self.state.next(self)

    def reject(self):
        self.state.reject(self)


# Usage
if __name__ == "__main__":
    document = Document()
    document.next()  # Sent for moderation
    document.reject()  # Rejected
    document.next()  # Cannot change state

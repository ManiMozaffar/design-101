class Document:
    def __init__(self):
        self.state = "Draft"


if __name__ == "__main__":
    document = Document()

    # Handling state transitions and actions in the main script
    if document.state == "Draft":
        document.state = "Moderation"
        print("Document sent for moderation.")
    elif document.state == "Moderation":
        document.state = "Published"
        print("Document published.")
    elif document.state == "Published":
        print("Document is already published.")
    elif document.state == "Rejected":
        print("Document is rejected and cannot change state.")

    # Handling rejection
    if document.state in ["Draft", "Moderation"]:
        document.state = "Rejected"
        print("Document rejected.")
    else:
        print("Cannot reject in current state.")

    # Attempting to move to the next state after rejection
    if document.state == "Draft":
        document.state = "Moderation"
        print("Document sent for moderation.")
    elif document.state == "Moderation":
        document.state = "Published"
        print("Document published.")
    elif document.state == "Published":
        print("Document is already published.")
    elif document.state == "Rejected":
        print("Document is rejected and cannot change state.")

from enum import StrEnum, auto
from typing import Literal, NewType

from pydantic import BaseModel

DocId = NewType("DocId", int)


class DocumentStates(StrEnum):
    DRAFT = auto()
    MODERATE = auto()
    PUBLISHED = auto()
    REJECTED = auto()


class StateBaseModel(BaseModel):
    name: str
    id: DocId


class DraftDocument(StateBaseModel):
    state: Literal[DocumentStates.DRAFT] = DocumentStates.DRAFT

    def next(self):
        return ModerationDocument(name=self.name, id=self.id)


class ModerationDocument(StateBaseModel):
    state: Literal[DocumentStates.MODERATE] = DocumentStates.MODERATE

    def next(self):
        return PublishedDocument(name=self.name, id=self.id)


class PublishedDocument(StateBaseModel):
    state: Literal[DocumentStates.PUBLISHED] = DocumentStates.PUBLISHED


class RejectedDocument(StateBaseModel):
    state: Literal[DocumentStates.REJECTED] = DocumentStates.REJECTED


def reject(document: DraftDocument | ModerationDocument) -> RejectedDocument:
    return RejectedDocument(
        state=DocumentStates.REJECTED, id=document.id, name=document.name
    )


# Usage
if __name__ == "__main__":
    document = DraftDocument(name="Git Over Here Overall Review", id=DocId(3))
    document = document.next()
    document = document.next()
    reject(
        document  # This should be marked as red in your IDE because it's not possible
    )

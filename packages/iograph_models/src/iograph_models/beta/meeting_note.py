from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MeetingNote(BaseModel):
	subpoints: Optional[list[MeetingNoteSubpoint]] = Field(alias="subpoints", default=None,)
	text: Optional[str] = Field(alias="text", default=None,)
	title: Optional[str] = Field(alias="title", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .meeting_note_subpoint import MeetingNoteSubpoint

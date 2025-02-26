from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RecentNotebookLinks(BaseModel):
	oneNoteClientUrl: Optional[ExternalLink] = Field(default=None,alias="oneNoteClientUrl",)
	oneNoteWebUrl: Optional[ExternalLink] = Field(default=None,alias="oneNoteWebUrl",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .external_link import ExternalLink
from .external_link import ExternalLink


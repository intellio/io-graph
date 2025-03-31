from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class RecentNotebook(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastAccessedTime: Optional[datetime] = Field(alias="lastAccessedTime", default=None,)
	links: Optional[RecentNotebookLinks] = Field(alias="links", default=None,)
	sourceService: Optional[OnenoteSourceService | str] = Field(alias="sourceService", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .recent_notebook_links import RecentNotebookLinks
from .onenote_source_service import OnenoteSourceService

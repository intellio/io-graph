from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class RecentNotebook(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastAccessedTime: Optional[datetime] = Field(default=None,alias="lastAccessedTime",)
	links: Optional[RecentNotebookLinks] = Field(default=None,alias="links",)
	sourceService: Optional[OnenoteSourceService] = Field(default=None,alias="sourceService",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .recent_notebook_links import RecentNotebookLinks
from .onenote_source_service import OnenoteSourceService


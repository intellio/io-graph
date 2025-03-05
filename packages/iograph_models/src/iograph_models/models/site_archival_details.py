from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SiteArchivalDetails(BaseModel):
	archiveStatus: Optional[SiteArchiveStatus] = Field(default=None,alias="archiveStatus",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .site_archive_status import SiteArchiveStatus


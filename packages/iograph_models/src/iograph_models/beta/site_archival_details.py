from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SiteArchivalDetails(BaseModel):
	archivedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="archivedBy",default=None,)
	archivedDateTime: Optional[datetime] = Field(alias="archivedDateTime",default=None,)
	archiveStatus: Optional[SiteArchiveStatus | str] = Field(alias="archiveStatus",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .identity_set import IdentitySet
from .site_archive_status import SiteArchiveStatus


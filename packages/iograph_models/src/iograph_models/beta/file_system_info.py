from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class FileSystemInfo(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastAccessedDateTime: Optional[datetime] = Field(alias="lastAccessedDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


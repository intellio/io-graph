from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DirectoryAuditCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[DirectoryAudit] = Field(alias="value",)

from .directory_audit import DirectoryAudit


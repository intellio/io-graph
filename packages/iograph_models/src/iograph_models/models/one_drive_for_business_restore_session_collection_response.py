from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OneDriveForBusinessRestoreSessionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[OneDriveForBusinessRestoreSession] = Field(alias="value",)

from .one_drive_for_business_restore_session import OneDriveForBusinessRestoreSession


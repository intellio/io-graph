from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OneDriveForBusinessRestoreSessionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[OneDriveForBusinessRestoreSession]] = Field(alias="value", default=None,)

from .one_drive_for_business_restore_session import OneDriveForBusinessRestoreSession


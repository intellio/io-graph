from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DriveRecipient(BaseModel):
	alias: Optional[str] = Field(default=None,alias="alias",)
	email: Optional[str] = Field(default=None,alias="email",)
	objectId: Optional[str] = Field(default=None,alias="objectId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)



from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DriveRecipient(BaseModel):
	alias: Optional[str] = Field(alias="alias", default=None,)
	email: Optional[str] = Field(alias="email", default=None,)
	objectId: Optional[str] = Field(alias="objectId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class PowerliftIncidentMetadata(BaseModel):
	application: Optional[str] = Field(alias="application", default=None,)
	clientVersion: Optional[str] = Field(alias="clientVersion", default=None,)
	createdAtDateTime: Optional[datetime] = Field(alias="createdAtDateTime", default=None,)
	easyId: Optional[str] = Field(alias="easyId", default=None,)
	fileNames: Optional[list[str]] = Field(alias="fileNames", default=None,)
	locale: Optional[str] = Field(alias="locale", default=None,)
	platform: Optional[str] = Field(alias="platform", default=None,)
	powerliftId: Optional[UUID] = Field(alias="powerliftId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


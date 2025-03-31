from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SelfSignedCertificate(BaseModel):
	customKeyIdentifier: Optional[str] = Field(alias="customKeyIdentifier", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	key: Optional[str] = Field(alias="key", default=None,)
	keyId: Optional[UUID] = Field(alias="keyId", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	thumbprint: Optional[str] = Field(alias="thumbprint", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	usage: Optional[str] = Field(alias="usage", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


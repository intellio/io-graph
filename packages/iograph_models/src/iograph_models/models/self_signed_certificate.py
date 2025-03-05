from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SelfSignedCertificate(BaseModel):
	customKeyIdentifier: Optional[str] = Field(default=None,alias="customKeyIdentifier",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	key: Optional[str] = Field(default=None,alias="key",)
	keyId: Optional[UUID] = Field(default=None,alias="keyId",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	thumbprint: Optional[str] = Field(default=None,alias="thumbprint",)
	type: Optional[str] = Field(default=None,alias="type",)
	usage: Optional[str] = Field(default=None,alias="usage",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)



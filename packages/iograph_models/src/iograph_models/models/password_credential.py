from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PasswordCredential(BaseModel):
	customKeyIdentifier: Optional[str] = Field(default=None,alias="customKeyIdentifier",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	hint: Optional[str] = Field(default=None,alias="hint",)
	keyId: Optional[UUID] = Field(default=None,alias="keyId",)
	secretText: Optional[str] = Field(default=None,alias="secretText",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)



from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class PasswordCredential(BaseModel):
	customKeyIdentifier: Optional[str] = Field(alias="customKeyIdentifier", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	hint: Optional[str] = Field(alias="hint", default=None,)
	keyId: Optional[UUID] = Field(alias="keyId", default=None,)
	secretText: Optional[str] = Field(alias="secretText", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


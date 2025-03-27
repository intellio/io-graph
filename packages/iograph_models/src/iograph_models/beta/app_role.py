from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppRole(BaseModel):
	allowedMemberTypes: Optional[list[str]] = Field(alias="allowedMemberTypes", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[UUID] = Field(alias="id", default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	origin: Optional[str] = Field(alias="origin", default=None,)
	value: Optional[str] = Field(alias="value", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)



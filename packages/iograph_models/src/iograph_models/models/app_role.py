from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field


class AppRole(BaseModel):
	allowedMemberTypes: list[str] = Field(alias="allowedMemberTypes",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	id: Optional[UUID] = Field(default=None,alias="id",)
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	origin: Optional[str] = Field(default=None,alias="origin",)
	value: Optional[str] = Field(default=None,alias="value",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)



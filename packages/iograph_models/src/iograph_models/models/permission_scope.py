from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PermissionScope(BaseModel):
	adminConsentDescription: Optional[str] = Field(default=None,alias="adminConsentDescription",)
	adminConsentDisplayName: Optional[str] = Field(default=None,alias="adminConsentDisplayName",)
	id: Optional[UUID] = Field(default=None,alias="id",)
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	origin: Optional[str] = Field(default=None,alias="origin",)
	type: Optional[str] = Field(default=None,alias="type",)
	userConsentDescription: Optional[str] = Field(default=None,alias="userConsentDescription",)
	userConsentDisplayName: Optional[str] = Field(default=None,alias="userConsentDisplayName",)
	value: Optional[str] = Field(default=None,alias="value",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)



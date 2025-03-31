from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field


class PermissionScope(BaseModel):
	adminConsentDescription: Optional[str] = Field(alias="adminConsentDescription", default=None,)
	adminConsentDisplayName: Optional[str] = Field(alias="adminConsentDisplayName", default=None,)
	id: Optional[UUID] = Field(alias="id", default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled", default=None,)
	origin: Optional[str] = Field(alias="origin", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	userConsentDescription: Optional[str] = Field(alias="userConsentDescription", default=None,)
	userConsentDisplayName: Optional[str] = Field(alias="userConsentDisplayName", default=None,)
	value: Optional[str] = Field(alias="value", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


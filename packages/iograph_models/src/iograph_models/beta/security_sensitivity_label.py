from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySensitivityLabel(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	color: Optional[str] = Field(alias="color", default=None,)
	contentFormats: Optional[list[str]] = Field(alias="contentFormats", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	hasProtection: Optional[bool] = Field(alias="hasProtection", default=None,)
	isActive: Optional[bool] = Field(alias="isActive", default=None,)
	isAppliable: Optional[bool] = Field(alias="isAppliable", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	sensitivity: Optional[int] = Field(alias="sensitivity", default=None,)
	tooltip: Optional[str] = Field(alias="tooltip", default=None,)
	parent: Optional[SecuritySensitivityLabel] = Field(alias="parent", default=None,)



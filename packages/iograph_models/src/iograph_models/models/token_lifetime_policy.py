from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class TokenLifetimePolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	definition: list[str] = Field(alias="definition",)
	isOrganizationDefault: Optional[bool] = Field(default=None,alias="isOrganizationDefault",)
	appliesTo: list[DirectoryObject] = Field(alias="appliesTo",)

from .directory_object import DirectoryObject


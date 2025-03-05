from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TokenIssuancePolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	definition: Optional[list[str]] = Field(default=None,alias="definition",)
	isOrganizationDefault: Optional[bool] = Field(default=None,alias="isOrganizationDefault",)
	appliesTo: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(default=None,alias="appliesTo",)

from .directory_object import DirectoryObject


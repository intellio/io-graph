from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TargetResource(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	groupType: Optional[GroupType] = Field(default=None,alias="groupType",)
	id: Optional[str] = Field(default=None,alias="id",)
	modifiedProperties: Optional[list[ModifiedProperty]] = Field(default=None,alias="modifiedProperties",)
	type: Optional[str] = Field(default=None,alias="type",)
	userPrincipalName: Optional[str] = Field(default=None,alias="userPrincipalName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .group_type import GroupType
from .modified_property import ModifiedProperty


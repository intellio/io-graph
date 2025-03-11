from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TargetResource(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	groupType: Optional[GroupType | str] = Field(alias="groupType",default=None,)
	id: Optional[str] = Field(alias="id",default=None,)
	modifiedProperties: Optional[list[ModifiedProperty]] = Field(alias="modifiedProperties",default=None,)
	type: Optional[str] = Field(alias="type",default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .group_type import GroupType
from .modified_property import ModifiedProperty


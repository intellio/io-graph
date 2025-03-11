from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class HomeRealmDiscoveryPolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	definition: Optional[list[str]] = Field(alias="definition",default=None,)
	isOrganizationDefault: Optional[bool] = Field(alias="isOrganizationDefault",default=None,)
	appliesTo: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="appliesTo",default=None,)

from .directory_object import DirectoryObject


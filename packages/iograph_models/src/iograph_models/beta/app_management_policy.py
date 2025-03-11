from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AppManagementPolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled",default=None,)
	restrictions: Optional[CustomAppManagementConfiguration] = Field(alias="restrictions",default=None,)
	appliesTo: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="appliesTo",default=None,)

from .custom_app_management_configuration import CustomAppManagementConfiguration
from .directory_object import DirectoryObject


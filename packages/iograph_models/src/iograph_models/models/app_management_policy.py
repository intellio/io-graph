from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AppManagementPolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	restrictions: Optional[CustomAppManagementConfiguration] = Field(default=None,alias="restrictions",)
	appliesTo: list[DirectoryObject] = Field(alias="appliesTo",)

from .custom_app_management_configuration import CustomAppManagementConfiguration
from .directory_object import DirectoryObject


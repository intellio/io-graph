from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class AccessPackageResourceEnvironment(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	connectionInfo: Optional[ConnectionInfo] = Field(default=None,alias="connectionInfo",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isDefaultEnvironment: Optional[bool] = Field(default=None,alias="isDefaultEnvironment",)
	modifiedDateTime: Optional[datetime] = Field(default=None,alias="modifiedDateTime",)
	originId: Optional[str] = Field(default=None,alias="originId",)
	originSystem: Optional[str] = Field(default=None,alias="originSystem",)
	resources: list[AccessPackageResource] = Field(alias="resources",)

from .connection_info import ConnectionInfo
from .access_package_resource import AccessPackageResource


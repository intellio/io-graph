from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AccessPackageResourceEnvironment(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	connectionInfo: Optional[ConnectionInfo] = Field(alias="connectionInfo", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isDefaultEnvironment: Optional[bool] = Field(alias="isDefaultEnvironment", default=None,)
	modifiedDateTime: Optional[datetime] = Field(alias="modifiedDateTime", default=None,)
	originId: Optional[str] = Field(alias="originId", default=None,)
	originSystem: Optional[str] = Field(alias="originSystem", default=None,)
	resources: Optional[list[AccessPackageResource]] = Field(alias="resources", default=None,)

from .connection_info import ConnectionInfo
from .access_package_resource import AccessPackageResource


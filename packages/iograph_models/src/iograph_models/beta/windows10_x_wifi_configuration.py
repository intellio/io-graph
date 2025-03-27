from __future__ import annotations
from uuid import UUID
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Windows10XWifiConfiguration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windows10XWifiConfiguration"] = Field(alias="@odata.type", default="#microsoft.graph.windows10XWifiConfiguration")
	creationDateTime: Optional[datetime] = Field(alias="creationDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	version: Optional[int] = Field(alias="version", default=None,)
	assignments: Optional[list[DeviceManagementResourceAccessProfileAssignment]] = Field(alias="assignments", default=None,)
	authenticationCertificateId: Optional[UUID] = Field(alias="authenticationCertificateId", default=None,)
	customXml: Optional[str] = Field(alias="customXml", default=None,)
	customXmlFileName: Optional[str] = Field(alias="customXmlFileName", default=None,)

from .device_management_resource_access_profile_assignment import DeviceManagementResourceAccessProfileAssignment


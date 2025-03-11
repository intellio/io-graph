from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DeviceTemplate(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	deviceAuthority: Optional[str] = Field(alias="deviceAuthority",default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer",default=None,)
	model: Optional[str] = Field(alias="model",default=None,)
	mutualTlsOauthConfigurationId: Optional[str] = Field(alias="mutualTlsOauthConfigurationId",default=None,)
	mutualTlsOauthConfigurationTenantId: Optional[str] = Field(alias="mutualTlsOauthConfigurationTenantId",default=None,)
	operatingSystem: Optional[str] = Field(alias="operatingSystem",default=None,)
	deviceInstances: Optional[list[Device]] = Field(alias="deviceInstances",default=None,)
	owners: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="owners",default=None,)

from .device import Device
from .directory_object import DirectoryObject


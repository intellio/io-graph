from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySensorSettings(BaseModel):
	description: Optional[str] = Field(default=None,alias="description",)
	domainControllerDnsNames: Optional[list[str]] = Field(default=None,alias="domainControllerDnsNames",)
	isDelayedDeploymentEnabled: Optional[bool] = Field(default=None,alias="isDelayedDeploymentEnabled",)
	networkAdapters: Optional[list[SecurityNetworkAdapter]] = Field(default=None,alias="networkAdapters",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .security_network_adapter import SecurityNetworkAdapter


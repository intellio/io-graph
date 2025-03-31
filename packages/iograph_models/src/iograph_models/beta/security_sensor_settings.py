from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecuritySensorSettings(BaseModel):
	description: Optional[str] = Field(alias="description", default=None,)
	domainControllerDnsNames: Optional[list[str]] = Field(alias="domainControllerDnsNames", default=None,)
	isDelayedDeploymentEnabled: Optional[bool] = Field(alias="isDelayedDeploymentEnabled", default=None,)
	networkAdapters: Optional[list[SecurityNetworkAdapter]] = Field(alias="networkAdapters", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .security_network_adapter import SecurityNetworkAdapter

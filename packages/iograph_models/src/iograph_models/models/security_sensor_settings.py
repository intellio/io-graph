from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecuritySensorSettings(BaseModel):
	description: Optional[str] = Field(default=None,alias="description",)
	domainControllerDnsNames: list[Optional[str]] = Field(alias="domainControllerDnsNames",)
	isDelayedDeploymentEnabled: Optional[bool] = Field(default=None,alias="isDelayedDeploymentEnabled",)
	networkAdapters: list[SecurityNetworkAdapter] = Field(alias="networkAdapters",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .security_network_adapter import SecurityNetworkAdapter


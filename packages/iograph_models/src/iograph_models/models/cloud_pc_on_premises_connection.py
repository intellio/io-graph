from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcOnPremisesConnection(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	adDomainName: Optional[str] = Field(default=None,alias="adDomainName",)
	adDomainPassword: Optional[str] = Field(default=None,alias="adDomainPassword",)
	adDomainUsername: Optional[str] = Field(default=None,alias="adDomainUsername",)
	alternateResourceUrl: Optional[str] = Field(default=None,alias="alternateResourceUrl",)
	connectionType: Optional[CloudPcOnPremisesConnectionType] = Field(default=None,alias="connectionType",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	healthCheckStatus: Optional[CloudPcOnPremisesConnectionStatus] = Field(default=None,alias="healthCheckStatus",)
	healthCheckStatusDetail: Optional[CloudPcOnPremisesConnectionStatusDetail] = Field(default=None,alias="healthCheckStatusDetail",)
	inUse: Optional[bool] = Field(default=None,alias="inUse",)
	organizationalUnit: Optional[str] = Field(default=None,alias="organizationalUnit",)
	resourceGroupId: Optional[str] = Field(default=None,alias="resourceGroupId",)
	subnetId: Optional[str] = Field(default=None,alias="subnetId",)
	subscriptionId: Optional[str] = Field(default=None,alias="subscriptionId",)
	subscriptionName: Optional[str] = Field(default=None,alias="subscriptionName",)
	virtualNetworkId: Optional[str] = Field(default=None,alias="virtualNetworkId",)
	virtualNetworkLocation: Optional[str] = Field(default=None,alias="virtualNetworkLocation",)

from .cloud_pc_on_premises_connection_type import CloudPcOnPremisesConnectionType
from .cloud_pc_on_premises_connection_status import CloudPcOnPremisesConnectionStatus
from .cloud_pc_on_premises_connection_status_detail import CloudPcOnPremisesConnectionStatusDetail


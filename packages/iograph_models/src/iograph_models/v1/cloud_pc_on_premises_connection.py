from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CloudPcOnPremisesConnection(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudPcOnPremisesConnection"] = Field(alias="@odata.type",)
	adDomainName: Optional[str] = Field(alias="adDomainName", default=None,)
	adDomainPassword: Optional[str] = Field(alias="adDomainPassword", default=None,)
	adDomainUsername: Optional[str] = Field(alias="adDomainUsername", default=None,)
	alternateResourceUrl: Optional[str] = Field(alias="alternateResourceUrl", default=None,)
	connectionType: Optional[CloudPcOnPremisesConnectionType | str] = Field(alias="connectionType", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	healthCheckStatus: Optional[CloudPcOnPremisesConnectionStatus | str] = Field(alias="healthCheckStatus", default=None,)
	healthCheckStatusDetail: Optional[CloudPcOnPremisesConnectionStatusDetail] = Field(alias="healthCheckStatusDetail", default=None,)
	inUse: Optional[bool] = Field(alias="inUse", default=None,)
	organizationalUnit: Optional[str] = Field(alias="organizationalUnit", default=None,)
	resourceGroupId: Optional[str] = Field(alias="resourceGroupId", default=None,)
	subnetId: Optional[str] = Field(alias="subnetId", default=None,)
	subscriptionId: Optional[str] = Field(alias="subscriptionId", default=None,)
	subscriptionName: Optional[str] = Field(alias="subscriptionName", default=None,)
	virtualNetworkId: Optional[str] = Field(alias="virtualNetworkId", default=None,)
	virtualNetworkLocation: Optional[str] = Field(alias="virtualNetworkLocation", default=None,)

from .cloud_pc_on_premises_connection_type import CloudPcOnPremisesConnectionType
from .cloud_pc_on_premises_connection_status import CloudPcOnPremisesConnectionStatus
from .cloud_pc_on_premises_connection_status_detail import CloudPcOnPremisesConnectionStatusDetail

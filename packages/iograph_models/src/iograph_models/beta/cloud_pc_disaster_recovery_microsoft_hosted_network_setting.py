from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CloudPcDisasterRecoveryMicrosoftHostedNetworkSetting(BaseModel):
	odata_type: Literal["#microsoft.graph.cloudPcDisasterRecoveryMicrosoftHostedNetworkSetting"] = Field(alias="@odata.type", default="#microsoft.graph.cloudPcDisasterRecoveryMicrosoftHostedNetworkSetting")
	regionGroup: Optional[CloudPcRegionGroup | str] = Field(alias="regionGroup", default=None,)
	regionName: Optional[str] = Field(alias="regionName", default=None,)

from .cloud_pc_region_group import CloudPcRegionGroup

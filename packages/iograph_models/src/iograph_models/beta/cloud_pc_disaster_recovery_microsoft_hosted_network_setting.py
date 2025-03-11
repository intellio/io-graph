from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcDisasterRecoveryMicrosoftHostedNetworkSetting(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	regionGroup: Optional[CloudPcRegionGroup | str] = Field(alias="regionGroup",default=None,)
	regionName: Optional[str] = Field(alias="regionName",default=None,)

from .cloud_pc_region_group import CloudPcRegionGroup


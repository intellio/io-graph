from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcCrossRegionDisasterRecoverySetting(BaseModel):
	crossRegionDisasterRecoveryEnabled: Optional[bool] = Field(alias="crossRegionDisasterRecoveryEnabled",default=None,)
	disasterRecoveryNetworkSetting: SerializeAsAny[Optional[CloudPcDisasterRecoveryNetworkSetting]] = Field(alias="disasterRecoveryNetworkSetting",default=None,)
	disasterRecoveryType: Optional[CloudPcDisasterRecoveryType | str] = Field(alias="disasterRecoveryType",default=None,)
	maintainCrossRegionRestorePointEnabled: Optional[bool] = Field(alias="maintainCrossRegionRestorePointEnabled",default=None,)
	userInitiatedDisasterRecoveryAllowed: Optional[bool] = Field(alias="userInitiatedDisasterRecoveryAllowed",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .cloud_pc_disaster_recovery_network_setting import CloudPcDisasterRecoveryNetworkSetting
from .cloud_pc_disaster_recovery_type import CloudPcDisasterRecoveryType


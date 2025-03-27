from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcCrossRegionDisasterRecoverySetting(BaseModel):
	crossRegionDisasterRecoveryEnabled: Optional[bool] = Field(alias="crossRegionDisasterRecoveryEnabled", default=None,)
	disasterRecoveryNetworkSetting: Optional[Union[CloudPcDisasterRecoveryAzureConnectionSetting, CloudPcDisasterRecoveryMicrosoftHostedNetworkSetting]] = Field(alias="disasterRecoveryNetworkSetting", default=None,discriminator="odata_type", )
	disasterRecoveryType: Optional[CloudPcDisasterRecoveryType | str] = Field(alias="disasterRecoveryType", default=None,)
	maintainCrossRegionRestorePointEnabled: Optional[bool] = Field(alias="maintainCrossRegionRestorePointEnabled", default=None,)
	userInitiatedDisasterRecoveryAllowed: Optional[bool] = Field(alias="userInitiatedDisasterRecoveryAllowed", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .cloud_pc_disaster_recovery_azure_connection_setting import CloudPcDisasterRecoveryAzureConnectionSetting
from .cloud_pc_disaster_recovery_microsoft_hosted_network_setting import CloudPcDisasterRecoveryMicrosoftHostedNetworkSetting
from .cloud_pc_disaster_recovery_type import CloudPcDisasterRecoveryType


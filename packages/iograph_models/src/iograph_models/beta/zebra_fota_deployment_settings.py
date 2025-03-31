from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ZebraFotaDeploymentSettings(BaseModel):
	batteryRuleMinimumBatteryLevelPercentage: Optional[int] = Field(alias="batteryRuleMinimumBatteryLevelPercentage", default=None,)
	batteryRuleRequireCharger: Optional[bool] = Field(alias="batteryRuleRequireCharger", default=None,)
	deviceModel: Optional[str] = Field(alias="deviceModel", default=None,)
	downloadRuleNetworkType: Optional[ZebraFotaNetworkType | str] = Field(alias="downloadRuleNetworkType", default=None,)
	downloadRuleStartDateTime: Optional[datetime] = Field(alias="downloadRuleStartDateTime", default=None,)
	firmwareTargetArtifactDescription: Optional[str] = Field(alias="firmwareTargetArtifactDescription", default=None,)
	firmwareTargetBoardSupportPackageVersion: Optional[str] = Field(alias="firmwareTargetBoardSupportPackageVersion", default=None,)
	firmwareTargetOsVersion: Optional[str] = Field(alias="firmwareTargetOsVersion", default=None,)
	firmwareTargetPatch: Optional[str] = Field(alias="firmwareTargetPatch", default=None,)
	installRuleStartDateTime: Optional[datetime] = Field(alias="installRuleStartDateTime", default=None,)
	installRuleWindowEndTime: Optional[str] = Field(alias="installRuleWindowEndTime", default=None,)
	installRuleWindowStartTime: Optional[str] = Field(alias="installRuleWindowStartTime", default=None,)
	scheduleDurationInDays: Optional[int] = Field(alias="scheduleDurationInDays", default=None,)
	scheduleMode: Optional[ZebraFotaScheduleMode | str] = Field(alias="scheduleMode", default=None,)
	timeZoneOffsetInMinutes: Optional[int] = Field(alias="timeZoneOffsetInMinutes", default=None,)
	updateType: Optional[ZebraFotaUpdateType | str] = Field(alias="updateType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .zebra_fota_network_type import ZebraFotaNetworkType
from .zebra_fota_schedule_mode import ZebraFotaScheduleMode
from .zebra_fota_update_type import ZebraFotaUpdateType

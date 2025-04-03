from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class MobileThreatDefenseConnector(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.mobileThreatDefenseConnector"] = Field(alias="@odata.type", default="#microsoft.graph.mobileThreatDefenseConnector")
	allowPartnerToCollectIOSApplicationMetadata: Optional[bool] = Field(alias="allowPartnerToCollectIOSApplicationMetadata", default=None,)
	allowPartnerToCollectIOSPersonalApplicationMetadata: Optional[bool] = Field(alias="allowPartnerToCollectIOSPersonalApplicationMetadata", default=None,)
	androidDeviceBlockedOnMissingPartnerData: Optional[bool] = Field(alias="androidDeviceBlockedOnMissingPartnerData", default=None,)
	androidEnabled: Optional[bool] = Field(alias="androidEnabled", default=None,)
	androidMobileApplicationManagementEnabled: Optional[bool] = Field(alias="androidMobileApplicationManagementEnabled", default=None,)
	iosDeviceBlockedOnMissingPartnerData: Optional[bool] = Field(alias="iosDeviceBlockedOnMissingPartnerData", default=None,)
	iosEnabled: Optional[bool] = Field(alias="iosEnabled", default=None,)
	iosMobileApplicationManagementEnabled: Optional[bool] = Field(alias="iosMobileApplicationManagementEnabled", default=None,)
	lastHeartbeatDateTime: Optional[datetime] = Field(alias="lastHeartbeatDateTime", default=None,)
	macDeviceBlockedOnMissingPartnerData: Optional[bool] = Field(alias="macDeviceBlockedOnMissingPartnerData", default=None,)
	macEnabled: Optional[bool] = Field(alias="macEnabled", default=None,)
	microsoftDefenderForEndpointAttachEnabled: Optional[bool] = Field(alias="microsoftDefenderForEndpointAttachEnabled", default=None,)
	partnerState: Optional[MobileThreatPartnerTenantState | str] = Field(alias="partnerState", default=None,)
	partnerUnresponsivenessThresholdInDays: Optional[int] = Field(alias="partnerUnresponsivenessThresholdInDays", default=None,)
	partnerUnsupportedOsVersionBlocked: Optional[bool] = Field(alias="partnerUnsupportedOsVersionBlocked", default=None,)
	windowsDeviceBlockedOnMissingPartnerData: Optional[bool] = Field(alias="windowsDeviceBlockedOnMissingPartnerData", default=None,)
	windowsEnabled: Optional[bool] = Field(alias="windowsEnabled", default=None,)
	windowsMobileApplicationManagementEnabled: Optional[bool] = Field(alias="windowsMobileApplicationManagementEnabled", default=None,)

from .mobile_threat_partner_tenant_state import MobileThreatPartnerTenantState

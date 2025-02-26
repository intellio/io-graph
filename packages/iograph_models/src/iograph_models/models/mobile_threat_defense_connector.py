from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class MobileThreatDefenseConnector(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	allowPartnerToCollectIOSApplicationMetadata: Optional[bool] = Field(default=None,alias="allowPartnerToCollectIOSApplicationMetadata",)
	allowPartnerToCollectIOSPersonalApplicationMetadata: Optional[bool] = Field(default=None,alias="allowPartnerToCollectIOSPersonalApplicationMetadata",)
	androidDeviceBlockedOnMissingPartnerData: Optional[bool] = Field(default=None,alias="androidDeviceBlockedOnMissingPartnerData",)
	androidEnabled: Optional[bool] = Field(default=None,alias="androidEnabled",)
	androidMobileApplicationManagementEnabled: Optional[bool] = Field(default=None,alias="androidMobileApplicationManagementEnabled",)
	iosDeviceBlockedOnMissingPartnerData: Optional[bool] = Field(default=None,alias="iosDeviceBlockedOnMissingPartnerData",)
	iosEnabled: Optional[bool] = Field(default=None,alias="iosEnabled",)
	iosMobileApplicationManagementEnabled: Optional[bool] = Field(default=None,alias="iosMobileApplicationManagementEnabled",)
	lastHeartbeatDateTime: Optional[datetime] = Field(default=None,alias="lastHeartbeatDateTime",)
	microsoftDefenderForEndpointAttachEnabled: Optional[bool] = Field(default=None,alias="microsoftDefenderForEndpointAttachEnabled",)
	partnerState: Optional[MobileThreatPartnerTenantState] = Field(default=None,alias="partnerState",)
	partnerUnresponsivenessThresholdInDays: Optional[int] = Field(default=None,alias="partnerUnresponsivenessThresholdInDays",)
	partnerUnsupportedOsVersionBlocked: Optional[bool] = Field(default=None,alias="partnerUnsupportedOsVersionBlocked",)
	windowsDeviceBlockedOnMissingPartnerData: Optional[bool] = Field(default=None,alias="windowsDeviceBlockedOnMissingPartnerData",)
	windowsEnabled: Optional[bool] = Field(default=None,alias="windowsEnabled",)

from .mobile_threat_partner_tenant_state import MobileThreatPartnerTenantState


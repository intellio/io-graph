from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class IosManagedAppRegistration(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	appIdentifier: Optional[MobileAppIdentifier] = Field(default=None,alias="appIdentifier",)
	applicationVersion: Optional[str] = Field(default=None,alias="applicationVersion",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	deviceName: Optional[str] = Field(default=None,alias="deviceName",)
	deviceTag: Optional[str] = Field(default=None,alias="deviceTag",)
	deviceType: Optional[str] = Field(default=None,alias="deviceType",)
	flaggedReasons: Optional[list[ManagedAppFlaggedReason]] = Field(default=None,alias="flaggedReasons",)
	lastSyncDateTime: Optional[datetime] = Field(default=None,alias="lastSyncDateTime",)
	managementSdkVersion: Optional[str] = Field(default=None,alias="managementSdkVersion",)
	platformVersion: Optional[str] = Field(default=None,alias="platformVersion",)
	userId: Optional[str] = Field(default=None,alias="userId",)
	version: Optional[str] = Field(default=None,alias="version",)
	appliedPolicies: Optional[list[ManagedAppPolicy]] = Field(default=None,alias="appliedPolicies",)
	intendedPolicies: Optional[list[ManagedAppPolicy]] = Field(default=None,alias="intendedPolicies",)
	operations: Optional[list[ManagedAppOperation]] = Field(default=None,alias="operations",)

from .mobile_app_identifier import MobileAppIdentifier
from .managed_app_flagged_reason import ManagedAppFlaggedReason
from .managed_app_policy import ManagedAppPolicy
from .managed_app_policy import ManagedAppPolicy
from .managed_app_operation import ManagedAppOperation


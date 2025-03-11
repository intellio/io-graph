from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IosManagedAppRegistration(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appIdentifier: SerializeAsAny[Optional[MobileAppIdentifier]] = Field(alias="appIdentifier",default=None,)
	applicationVersion: Optional[str] = Field(alias="applicationVersion",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	deviceName: Optional[str] = Field(alias="deviceName",default=None,)
	deviceTag: Optional[str] = Field(alias="deviceTag",default=None,)
	deviceType: Optional[str] = Field(alias="deviceType",default=None,)
	flaggedReasons: Optional[list[ManagedAppFlaggedReason | str]] = Field(alias="flaggedReasons",default=None,)
	lastSyncDateTime: Optional[datetime] = Field(alias="lastSyncDateTime",default=None,)
	managementSdkVersion: Optional[str] = Field(alias="managementSdkVersion",default=None,)
	platformVersion: Optional[str] = Field(alias="platformVersion",default=None,)
	userId: Optional[str] = Field(alias="userId",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)
	appliedPolicies: SerializeAsAny[Optional[list[ManagedAppPolicy]]] = Field(alias="appliedPolicies",default=None,)
	intendedPolicies: SerializeAsAny[Optional[list[ManagedAppPolicy]]] = Field(alias="intendedPolicies",default=None,)
	operations: Optional[list[ManagedAppOperation]] = Field(alias="operations",default=None,)

from .mobile_app_identifier import MobileAppIdentifier
from .managed_app_flagged_reason import ManagedAppFlaggedReason
from .managed_app_policy import ManagedAppPolicy
from .managed_app_policy import ManagedAppPolicy
from .managed_app_operation import ManagedAppOperation


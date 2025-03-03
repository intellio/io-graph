from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class OneDriveForBusinessProtectionPolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	retentionSettings: Optional[list[RetentionSetting]] = Field(default=None,alias="retentionSettings",)
	status: Optional[ProtectionPolicyStatus] = Field(default=None,alias="status",)
	driveInclusionRules: Optional[list[DriveProtectionRule]] = Field(default=None,alias="driveInclusionRules",)
	driveProtectionUnits: Optional[list[DriveProtectionUnit]] = Field(default=None,alias="driveProtectionUnits",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .retention_setting import RetentionSetting
from .protection_policy_status import ProtectionPolicyStatus
from .drive_protection_rule import DriveProtectionRule
from .drive_protection_unit import DriveProtectionUnit


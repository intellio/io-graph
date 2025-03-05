from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class OneDriveForBusinessProtectionPolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	retentionSettings: Optional[list[RetentionSetting]] = Field(alias="retentionSettings",default=None,)
	status: Optional[str | ProtectionPolicyStatus] = Field(alias="status",default=None,)
	driveInclusionRules: Optional[list[DriveProtectionRule]] = Field(alias="driveInclusionRules",default=None,)
	driveProtectionUnits: Optional[list[DriveProtectionUnit]] = Field(alias="driveProtectionUnits",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .retention_setting import RetentionSetting
from .protection_policy_status import ProtectionPolicyStatus
from .drive_protection_rule import DriveProtectionRule
from .drive_protection_unit import DriveProtectionUnit


from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SharePointProtectionPolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: Optional[IdentitySet] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	retentionSettings: Optional[list[RetentionSetting]] = Field(default=None,alias="retentionSettings",)
	status: Optional[ProtectionPolicyStatus] = Field(default=None,alias="status",)
	siteInclusionRules: Optional[list[SiteProtectionRule]] = Field(default=None,alias="siteInclusionRules",)
	siteProtectionUnits: Optional[list[SiteProtectionUnit]] = Field(default=None,alias="siteProtectionUnits",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .retention_setting import RetentionSetting
from .protection_policy_status import ProtectionPolicyStatus
from .site_protection_rule import SiteProtectionRule
from .site_protection_unit import SiteProtectionUnit


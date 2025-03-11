from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SharePointProtectionPolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	retentionSettings: Optional[list[RetentionSetting]] = Field(alias="retentionSettings",default=None,)
	status: Optional[ProtectionPolicyStatus | str] = Field(alias="status",default=None,)
	siteInclusionRules: Optional[list[SiteProtectionRule]] = Field(alias="siteInclusionRules",default=None,)
	siteProtectionUnits: Optional[list[SiteProtectionUnit]] = Field(alias="siteProtectionUnits",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .retention_setting import RetentionSetting
from .protection_policy_status import ProtectionPolicyStatus
from .site_protection_rule import SiteProtectionRule
from .site_protection_unit import SiteProtectionUnit


from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryHoldPolicy(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	status: Optional[SecurityPolicyStatus | str] = Field(alias="status",default=None,)
	contentQuery: Optional[str] = Field(alias="contentQuery",default=None,)
	errors: Optional[list[str]] = Field(alias="errors",default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled",default=None,)
	siteSources: Optional[list[SecuritySiteSource]] = Field(alias="siteSources",default=None,)
	userSources: Optional[list[SecurityUserSource]] = Field(alias="userSources",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .security_policy_status import SecurityPolicyStatus
from .security_site_source import SecuritySiteSource
from .security_user_source import SecurityUserSource


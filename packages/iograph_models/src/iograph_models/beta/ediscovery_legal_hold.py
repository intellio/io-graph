from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EdiscoveryLegalHold(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	contentQuery: Optional[str] = Field(alias="contentQuery",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	errors: Optional[list[str]] = Field(alias="errors",default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	status: Optional[EdiscoveryLegalHoldStatus | str] = Field(alias="status",default=None,)
	siteSources: Optional[list[EdiscoverySiteSource]] = Field(alias="siteSources",default=None,)
	unifiedGroupSources: Optional[list[EdiscoveryUnifiedGroupSource]] = Field(alias="unifiedGroupSources",default=None,)
	userSources: Optional[list[EdiscoveryUserSource]] = Field(alias="userSources",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet
from .ediscovery_legal_hold_status import EdiscoveryLegalHoldStatus
from .ediscovery_site_source import EdiscoverySiteSource
from .ediscovery_unified_group_source import EdiscoveryUnifiedGroupSource
from .ediscovery_user_source import EdiscoveryUserSource


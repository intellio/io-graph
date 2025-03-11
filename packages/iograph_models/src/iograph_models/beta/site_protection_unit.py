from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SiteProtectionUnit(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	error: Optional[PublicError] = Field(alias="error",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	policyId: Optional[str] = Field(alias="policyId",default=None,)
	protectionSources: Optional[ProtectionSource | str] = Field(alias="protectionSources",default=None,)
	status: Optional[ProtectionUnitStatus | str] = Field(alias="status",default=None,)
	siteId: Optional[str] = Field(alias="siteId",default=None,)
	siteName: Optional[str] = Field(alias="siteName",default=None,)
	siteWebUrl: Optional[str] = Field(alias="siteWebUrl",default=None,)

from .identity_set import IdentitySet
from .public_error import PublicError
from .identity_set import IdentitySet
from .protection_source import ProtectionSource
from .protection_unit_status import ProtectionUnitStatus


from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SiteProtectionUnit(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	error: Optional[PublicError] = Field(default=None,alias="error",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	policyId: Optional[str] = Field(default=None,alias="policyId",)
	status: Optional[ProtectionUnitStatus] = Field(default=None,alias="status",)
	siteId: Optional[str] = Field(default=None,alias="siteId",)
	siteName: Optional[str] = Field(default=None,alias="siteName",)
	siteWebUrl: Optional[str] = Field(default=None,alias="siteWebUrl",)

from .identity_set import IdentitySet
from .public_error import PublicError
from .identity_set import IdentitySet
from .protection_unit_status import ProtectionUnitStatus


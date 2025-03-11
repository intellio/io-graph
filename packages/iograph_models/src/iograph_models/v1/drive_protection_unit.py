from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class DriveProtectionUnit(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	error: Optional[PublicError] = Field(alias="error",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	policyId: Optional[str] = Field(alias="policyId",default=None,)
	status: Optional[ProtectionUnitStatus | str] = Field(alias="status",default=None,)
	directoryObjectId: Optional[str] = Field(alias="directoryObjectId",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	email: Optional[str] = Field(alias="email",default=None,)

from .identity_set import IdentitySet
from .public_error import PublicError
from .identity_set import IdentitySet
from .protection_unit_status import ProtectionUnitStatus


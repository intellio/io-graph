from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MailboxProtectionUnitsBulkAdditionJob(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	error: Optional[PublicError] = Field(alias="error",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	status: Optional[ProtectionUnitsBulkJobStatus | str] = Field(alias="status",default=None,)
	directoryObjectIds: Optional[list[str]] = Field(alias="directoryObjectIds",default=None,)
	mailboxes: Optional[list[str]] = Field(alias="mailboxes",default=None,)

from .identity_set import IdentitySet
from .public_error import PublicError
from .identity_set import IdentitySet
from .protection_units_bulk_job_status import ProtectionUnitsBulkJobStatus


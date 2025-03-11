from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ServiceStatus(BaseModel):
	backupServiceConsumer: Optional[BackupServiceConsumer | str] = Field(alias="backupServiceConsumer",default=None,)
	disableReason: Optional[DisableReason | str] = Field(alias="disableReason",default=None,)
	gracePeriodDateTime: Optional[datetime] = Field(alias="gracePeriodDateTime",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	restoreAllowedTillDateTime: Optional[datetime] = Field(alias="restoreAllowedTillDateTime",default=None,)
	status: Optional[BackupServiceStatus | str] = Field(alias="status",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .backup_service_consumer import BackupServiceConsumer
from .disable_reason import DisableReason
from .identity_set import IdentitySet
from .backup_service_status import BackupServiceStatus


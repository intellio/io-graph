from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ServiceStatus(BaseModel):
	backupServiceConsumer: Optional[BackupServiceConsumer] = Field(default=None,alias="backupServiceConsumer",)
	disableReason: Optional[DisableReason] = Field(default=None,alias="disableReason",)
	gracePeriodDateTime: Optional[datetime] = Field(default=None,alias="gracePeriodDateTime",)
	lastModifiedBy: Optional[IdentitySet] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	restoreAllowedTillDateTime: Optional[datetime] = Field(default=None,alias="restoreAllowedTillDateTime",)
	status: Optional[BackupServiceStatus] = Field(default=None,alias="status",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .backup_service_consumer import BackupServiceConsumer
from .disable_reason import DisableReason
from .identity_set import IdentitySet
from .backup_service_status import BackupServiceStatus


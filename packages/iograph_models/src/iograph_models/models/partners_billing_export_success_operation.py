from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class PartnersBillingExportSuccessOperation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	lastActionDateTime: Optional[datetime] = Field(default=None,alias="lastActionDateTime",)
	status: Optional[LongRunningOperationStatus] = Field(default=None,alias="status",)
	resourceLocation: Optional[PartnersBillingManifest] = Field(default=None,alias="resourceLocation",)

from .long_running_operation_status import LongRunningOperationStatus
from .partners_billing_manifest import PartnersBillingManifest


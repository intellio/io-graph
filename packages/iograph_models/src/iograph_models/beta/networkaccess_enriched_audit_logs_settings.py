from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessEnrichedAuditLogsSettings(BaseModel):
	status: Optional[NetworkaccessStatus | str] = Field(alias="status",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .networkaccess_status import NetworkaccessStatus


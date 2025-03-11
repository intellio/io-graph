from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessFilteringPolicyLink(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	state: Optional[NetworkaccessStatus | str] = Field(alias="state",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)
	policy: SerializeAsAny[Optional[NetworkaccessPolicy]] = Field(alias="policy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	loggingState: Optional[NetworkaccessStatus | str] = Field(alias="loggingState",default=None,)
	priority: Optional[int] = Field(alias="priority",default=None,)

from .networkaccess_status import NetworkaccessStatus
from .networkaccess_policy import NetworkaccessPolicy
from .networkaccess_status import NetworkaccessStatus


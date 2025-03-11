from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessForwardingPolicyLink(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	state: Optional[NetworkaccessStatus | str] = Field(alias="state",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)
	policy: SerializeAsAny[Optional[NetworkaccessPolicy]] = Field(alias="policy",default=None,)

from .networkaccess_status import NetworkaccessStatus
from .networkaccess_policy import NetworkaccessPolicy


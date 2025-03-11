from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessForwardingOptions(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	skipDnsLookupState: Optional[NetworkaccessStatus | str] = Field(alias="skipDnsLookupState",default=None,)

from .networkaccess_status import NetworkaccessStatus


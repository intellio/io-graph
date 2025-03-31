from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class NetworkaccessForwardingOptions(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.networkaccess.forwardingOptions"] = Field(alias="@odata.type",)
	skipDnsLookupState: Optional[NetworkaccessStatus | str] = Field(alias="skipDnsLookupState", default=None,)

from .networkaccess_status import NetworkaccessStatus

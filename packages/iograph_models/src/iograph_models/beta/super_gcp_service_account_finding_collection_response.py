from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SuperGcpServiceAccountFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[SuperGcpServiceAccountFinding]] = Field(alias="value",default=None,)

from .super_gcp_service_account_finding import SuperGcpServiceAccountFinding


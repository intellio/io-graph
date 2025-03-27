from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OverprovisionedGcpServiceAccountFindingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[OverprovisionedGcpServiceAccountFinding]] = Field(alias="value", default=None,)

from .overprovisioned_gcp_service_account_finding import OverprovisionedGcpServiceAccountFinding


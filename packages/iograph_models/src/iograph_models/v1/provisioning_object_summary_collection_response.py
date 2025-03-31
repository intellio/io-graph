from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ProvisioningObjectSummaryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ProvisioningObjectSummary]] = Field(alias="value", default=None,)

from .provisioning_object_summary import ProvisioningObjectSummary

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityEdiscoveryPurgeDataOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[SecurityEdiscoveryPurgeDataOperation]] = Field(default=None,alias="value",)

from .security_ediscovery_purge_data_operation import SecurityEdiscoveryPurgeDataOperation


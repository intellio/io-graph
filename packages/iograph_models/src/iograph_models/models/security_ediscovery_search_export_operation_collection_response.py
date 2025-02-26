from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityEdiscoverySearchExportOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[SecurityEdiscoverySearchExportOperation] = Field(alias="value",)

from .security_ediscovery_search_export_operation import SecurityEdiscoverySearchExportOperation


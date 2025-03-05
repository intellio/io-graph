from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoverySearchExportOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[SecurityEdiscoverySearchExportOperation]] = Field(alias="value",default=None,)

from .security_ediscovery_search_export_operation import SecurityEdiscoverySearchExportOperation


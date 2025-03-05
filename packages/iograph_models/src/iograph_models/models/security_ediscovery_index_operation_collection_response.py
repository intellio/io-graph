from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryIndexOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[SecurityEdiscoveryIndexOperation]] = Field(alias="value",default=None,)

from .security_ediscovery_index_operation import SecurityEdiscoveryIndexOperation


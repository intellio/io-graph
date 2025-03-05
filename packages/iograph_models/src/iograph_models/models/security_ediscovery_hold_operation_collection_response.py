from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityEdiscoveryHoldOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[SecurityEdiscoveryHoldOperation]] = Field(default=None,alias="value",)

from .security_ediscovery_hold_operation import SecurityEdiscoveryHoldOperation


from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ClaimsMappingPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[ClaimsMappingPolicy]] = Field(alias="value",default=None,)

from .claims_mapping_policy import ClaimsMappingPolicy


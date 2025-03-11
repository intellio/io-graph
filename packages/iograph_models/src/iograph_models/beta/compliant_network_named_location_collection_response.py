from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CompliantNetworkNamedLocationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[CompliantNetworkNamedLocation]] = Field(alias="value",default=None,)

from .compliant_network_named_location import CompliantNetworkNamedLocation


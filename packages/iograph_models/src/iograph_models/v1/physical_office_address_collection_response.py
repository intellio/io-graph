from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PhysicalOfficeAddressCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[PhysicalOfficeAddress]] = Field(alias="value",default=None,)

from .physical_office_address import PhysicalOfficeAddress


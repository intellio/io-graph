from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class PhysicalOfficeAddressCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[PhysicalOfficeAddress] = Field(alias="value",)

from .physical_office_address import PhysicalOfficeAddress


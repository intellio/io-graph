from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosVppEBookAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[IosVppEBookAssignment]] = Field(alias="value", default=None,)

from .ios_vpp_e_book_assignment import IosVppEBookAssignment

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AddInCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[AddIn]] = Field(default=None,alias="value",)

from .add_in import AddIn


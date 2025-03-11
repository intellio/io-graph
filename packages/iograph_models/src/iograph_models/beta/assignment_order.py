from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AssignmentOrder(BaseModel):
	order: Optional[list[str]] = Field(alias="order",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)



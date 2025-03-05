from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AssignmentOrder(BaseModel):
	order: Optional[list[str]] = Field(default=None,alias="order",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)



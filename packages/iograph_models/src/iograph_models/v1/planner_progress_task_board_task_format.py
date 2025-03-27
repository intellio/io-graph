from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerProgressTaskBoardTaskFormat(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	orderHint: Optional[str] = Field(alias="orderHint", default=None,)



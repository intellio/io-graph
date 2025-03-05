from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerUserIds(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)



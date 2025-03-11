from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class PlannerFavoritePlanReference(BaseModel):
	orderHint: Optional[str] = Field(alias="orderHint",default=None,)
	planTitle: Optional[str] = Field(alias="planTitle",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)



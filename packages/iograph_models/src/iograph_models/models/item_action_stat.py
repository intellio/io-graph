from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ItemActionStat(BaseModel):
	actionCount: Optional[int] = Field(default=None,alias="actionCount",)
	actorCount: Optional[int] = Field(default=None,alias="actorCount",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)



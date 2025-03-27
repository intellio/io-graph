from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ItemActionStat(BaseModel):
	actionCount: Optional[int] = Field(alias="actionCount", default=None,)
	actorCount: Optional[int] = Field(alias="actorCount", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)



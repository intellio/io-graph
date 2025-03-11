from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RiskProfile(BaseModel):
	humanCount: Optional[int] = Field(alias="humanCount",default=None,)
	nonHumanCount: Optional[int] = Field(alias="nonHumanCount",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)



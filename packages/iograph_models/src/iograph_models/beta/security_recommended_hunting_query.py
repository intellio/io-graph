from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityRecommendedHuntingQuery(BaseModel):
	kqlText: Optional[str] = Field(alias="kqlText", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)



from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataSimplePasswordSettings(BaseModel):
	odata_type: Literal["#microsoft.graph.industryData.simplePasswordSettings"] = Field(alias="@odata.type", default="#microsoft.graph.industryData.simplePasswordSettings")
	password: Optional[str] = Field(alias="password", default=None,)



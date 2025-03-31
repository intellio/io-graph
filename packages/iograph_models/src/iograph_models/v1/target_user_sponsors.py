from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class TargetUserSponsors(BaseModel):
	odata_type: Literal["#microsoft.graph.targetUserSponsors"] = Field(alias="@odata.type", default="#microsoft.graph.targetUserSponsors")


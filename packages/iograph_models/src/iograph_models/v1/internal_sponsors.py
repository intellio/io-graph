from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class InternalSponsors(BaseModel):
	odata_type: Literal["#microsoft.graph.internalSponsors"] = Field(alias="@odata.type", default="#microsoft.graph.internalSponsors")


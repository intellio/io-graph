from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class EdIdentitySource(BaseModel):
	odata_type: Literal["#microsoft.graph.edIdentitySource"] = Field(alias="@odata.type", default="#microsoft.graph.edIdentitySource")


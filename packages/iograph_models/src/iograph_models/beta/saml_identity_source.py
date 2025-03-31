from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SamlIdentitySource(BaseModel):
	odata_type: Literal["#microsoft.graph.samlIdentitySource"] = Field(alias="@odata.type", default="#microsoft.graph.samlIdentitySource")


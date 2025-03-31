from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class WafAllowedHeadersDictionary(BaseModel):
	odata_type: Literal["#microsoft.graph.wafAllowedHeadersDictionary"] = Field(alias="@odata.type",)


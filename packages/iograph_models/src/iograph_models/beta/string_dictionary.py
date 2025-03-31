from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class StringDictionary(BaseModel):
	odata_type: Literal["#microsoft.graph.stringDictionary"] = Field(alias="@odata.type",)


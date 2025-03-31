from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class ResultTemplateDictionary(BaseModel):
	odata_type: Literal["#microsoft.graph.resultTemplateDictionary"] = Field(alias="@odata.type",)


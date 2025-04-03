from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class PlannerFormsDictionary(BaseModel):
	odata_type: Literal["#microsoft.graph.plannerFormsDictionary"] = Field(alias="@odata.type", default="#microsoft.graph.plannerFormsDictionary")


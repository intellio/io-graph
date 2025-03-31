from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class RemoveAccessApplyAction(BaseModel):
	odata_type: Literal["#microsoft.graph.removeAccessApplyAction"] = Field(alias="@odata.type", default="#microsoft.graph.removeAccessApplyAction")


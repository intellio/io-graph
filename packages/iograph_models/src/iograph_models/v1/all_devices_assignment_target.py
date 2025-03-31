from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class AllDevicesAssignmentTarget(BaseModel):
	odata_type: Literal["#microsoft.graph.allDevicesAssignmentTarget"] = Field(alias="@odata.type", default="#microsoft.graph.allDevicesAssignmentTarget")


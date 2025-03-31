from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class DisableAndDeleteUserApplyAction(BaseModel):
	odata_type: Literal["#microsoft.graph.disableAndDeleteUserApplyAction"] = Field(alias="@odata.type", default="#microsoft.graph.disableAndDeleteUserApplyAction")


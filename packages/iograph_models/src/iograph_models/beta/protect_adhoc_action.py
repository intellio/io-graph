from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class ProtectAdhocAction(BaseModel):
	odata_type: Literal["#microsoft.graph.protectAdhocAction"] = Field(alias="@odata.type", default="#microsoft.graph.protectAdhocAction")


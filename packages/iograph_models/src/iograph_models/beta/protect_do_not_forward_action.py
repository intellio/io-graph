from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class ProtectDoNotForwardAction(BaseModel):
	odata_type: Literal["#microsoft.graph.protectDoNotForwardAction"] = Field(alias="@odata.type", default="#microsoft.graph.protectDoNotForwardAction")



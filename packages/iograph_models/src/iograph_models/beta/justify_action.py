from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class JustifyAction(BaseModel):
	odata_type: Literal["#microsoft.graph.justifyAction"] = Field(alias="@odata.type", default="#microsoft.graph.justifyAction")



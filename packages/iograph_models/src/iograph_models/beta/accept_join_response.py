from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AcceptJoinResponse(BaseModel):
	odata_type: Literal["#microsoft.graph.acceptJoinResponse"] = Field(alias="@odata.type", default="#microsoft.graph.acceptJoinResponse")



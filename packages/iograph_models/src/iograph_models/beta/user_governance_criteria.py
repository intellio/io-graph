from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class UserGovernanceCriteria(BaseModel):
	odata_type: Literal["#microsoft.graph.userGovernanceCriteria"] = Field(alias="@odata.type", default="#microsoft.graph.userGovernanceCriteria")
	userId: Optional[str] = Field(alias="userId", default=None,)



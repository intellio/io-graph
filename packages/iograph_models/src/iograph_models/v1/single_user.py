from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SingleUser(BaseModel):
	odata_type: Literal["#microsoft.graph.singleUser"] = Field(alias="@odata.type", default="#microsoft.graph.singleUser")
	description: Optional[str] = Field(alias="description", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)



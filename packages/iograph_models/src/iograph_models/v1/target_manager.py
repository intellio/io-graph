from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class TargetManager(BaseModel):
	odata_type: Literal["#microsoft.graph.targetManager"] = Field(alias="@odata.type", default="#microsoft.graph.targetManager")
	managerLevel: Optional[int] = Field(alias="managerLevel", default=None,)



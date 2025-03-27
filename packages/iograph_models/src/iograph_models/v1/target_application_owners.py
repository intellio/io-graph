from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class TargetApplicationOwners(BaseModel):
	odata_type: Literal["#microsoft.graph.targetApplicationOwners"] = Field(alias="@odata.type", default="#microsoft.graph.targetApplicationOwners")



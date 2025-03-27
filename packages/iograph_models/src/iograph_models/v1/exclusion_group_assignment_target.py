from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class ExclusionGroupAssignmentTarget(BaseModel):
	odata_type: Literal["#microsoft.graph.exclusionGroupAssignmentTarget"] = Field(alias="@odata.type", default="#microsoft.graph.exclusionGroupAssignmentTarget")
	groupId: Optional[str] = Field(alias="groupId", default=None,)



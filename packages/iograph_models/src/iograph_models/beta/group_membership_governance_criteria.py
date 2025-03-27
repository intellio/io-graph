from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class GroupMembershipGovernanceCriteria(BaseModel):
	odata_type: Literal["#microsoft.graph.groupMembershipGovernanceCriteria"] = Field(alias="@odata.type", default="#microsoft.graph.groupMembershipGovernanceCriteria")
	groupId: Optional[str] = Field(alias="groupId", default=None,)



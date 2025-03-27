from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceGroupBasedSubjectSet(BaseModel):
	odata_type: Literal["#microsoft.graph.identityGovernance.groupBasedSubjectSet"] = Field(alias="@odata.type", default="#microsoft.graph.identityGovernance.groupBasedSubjectSet")
	groups: Optional[list[Group]] = Field(alias="groups", default=None,)

from .group import Group


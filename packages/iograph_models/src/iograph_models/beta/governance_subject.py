from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class GovernanceSubject(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.governanceSubject"] = Field(alias="@odata.type", default="#microsoft.graph.governanceSubject")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	email: Optional[str] = Field(alias="email", default=None,)
	principalName: Optional[str] = Field(alias="principalName", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)


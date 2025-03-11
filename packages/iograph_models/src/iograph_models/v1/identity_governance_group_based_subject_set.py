from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernanceGroupBasedSubjectSet(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	groups: Optional[list[Group]] = Field(alias="groups",default=None,)

from .group import Group


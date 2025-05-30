from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PrivilegedAccessRoot(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.privilegedAccessRoot"] = Field(alias="@odata.type", default="#microsoft.graph.privilegedAccessRoot")
	group: Optional[PrivilegedAccessGroup] = Field(alias="group", default=None,)

from .privileged_access_group import PrivilegedAccessGroup

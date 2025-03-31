from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class PermissionsDefinitionGcpRole(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.permissionsDefinitionGcpRole"] = Field(alias="@odata.type",)


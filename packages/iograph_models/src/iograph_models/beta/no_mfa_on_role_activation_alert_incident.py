from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class NoMfaOnRoleActivationAlertIncident(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.noMfaOnRoleActivationAlertIncident"] = Field(alias="@odata.type", default="#microsoft.graph.noMfaOnRoleActivationAlertIncident")
	roleDisplayName: Optional[str] = Field(alias="roleDisplayName", default=None,)
	roleTemplateId: Optional[str] = Field(alias="roleTemplateId", default=None,)


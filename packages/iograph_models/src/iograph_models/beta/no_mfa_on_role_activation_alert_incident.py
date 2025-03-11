from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class NoMfaOnRoleActivationAlertIncident(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	roleDisplayName: Optional[str] = Field(alias="roleDisplayName",default=None,)
	roleTemplateId: Optional[str] = Field(alias="roleTemplateId",default=None,)



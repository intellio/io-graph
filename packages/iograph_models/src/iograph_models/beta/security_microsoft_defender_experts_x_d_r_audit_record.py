from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMicrosoftDefenderExpertsXDRAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.microsoftDefenderExpertsXDRAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.microsoftDefenderExpertsXDRAuditRecord")



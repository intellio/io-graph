from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityProjectForTheWebAssignedToMeSettingsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.projectForTheWebAssignedToMeSettingsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.projectForTheWebAssignedToMeSettingsAuditRecord")



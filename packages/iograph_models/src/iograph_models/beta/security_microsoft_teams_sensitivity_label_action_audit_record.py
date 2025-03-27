from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMicrosoftTeamsSensitivityLabelActionAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.microsoftTeamsSensitivityLabelActionAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.microsoftTeamsSensitivityLabelActionAuditRecord")



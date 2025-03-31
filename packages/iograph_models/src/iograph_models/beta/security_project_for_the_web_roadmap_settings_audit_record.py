from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityProjectForTheWebRoadmapSettingsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.projectForTheWebRoadmapSettingsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.projectForTheWebRoadmapSettingsAuditRecord")


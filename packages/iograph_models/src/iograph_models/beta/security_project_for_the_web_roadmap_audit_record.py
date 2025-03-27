from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityProjectForTheWebRoadmapAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.projectForTheWebRoadmapAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.projectForTheWebRoadmapAuditRecord")



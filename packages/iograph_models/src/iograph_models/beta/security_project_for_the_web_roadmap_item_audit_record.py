from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityProjectForTheWebRoadmapItemAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.projectForTheWebRoadmapItemAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.projectForTheWebRoadmapItemAuditRecord")



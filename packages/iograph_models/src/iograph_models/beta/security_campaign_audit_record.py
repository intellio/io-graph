from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityCampaignAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.campaignAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.campaignAuditRecord")



from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityPrivacyPortalAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.privacyPortalAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.privacyPortalAuditRecord")



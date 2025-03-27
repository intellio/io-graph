from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityPrivacyDataMatchAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.privacyDataMatchAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.privacyDataMatchAuditRecord")



from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMicrosoftPurviewPrivacyAuditEvent(BaseModel):
	odata_type: Literal["#microsoft.graph.security.microsoftPurviewPrivacyAuditEvent"] = Field(alias="@odata.type", default="#microsoft.graph.security.microsoftPurviewPrivacyAuditEvent")



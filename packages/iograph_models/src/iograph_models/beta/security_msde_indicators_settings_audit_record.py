from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMsdeIndicatorsSettingsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.msdeIndicatorsSettingsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.msdeIndicatorsSettingsAuditRecord")



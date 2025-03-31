from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMsdeGeneralSettingsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.msdeGeneralSettingsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.msdeGeneralSettingsAuditRecord")


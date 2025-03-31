from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMsdeRolesSettingsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.msdeRolesSettingsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.msdeRolesSettingsAuditRecord")


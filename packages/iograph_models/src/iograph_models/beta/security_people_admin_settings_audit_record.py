from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityPeopleAdminSettingsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.peopleAdminSettingsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.peopleAdminSettingsAuditRecord")


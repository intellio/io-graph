from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityWdatpAlertsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.wdatpAlertsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.wdatpAlertsAuditRecord")



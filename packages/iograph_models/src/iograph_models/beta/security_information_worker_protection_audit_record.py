from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityInformationWorkerProtectionAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.informationWorkerProtectionAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.informationWorkerProtectionAuditRecord")



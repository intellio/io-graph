from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDataShareOperationAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.dataShareOperationAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.dataShareOperationAuditRecord")



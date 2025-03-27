from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMdatpAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mdatpAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.mdatpAuditRecord")



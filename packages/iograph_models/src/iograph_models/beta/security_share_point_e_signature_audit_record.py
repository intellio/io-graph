from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecuritySharePointESignatureAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.sharePointESignatureAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.sharePointESignatureAuditRecord")



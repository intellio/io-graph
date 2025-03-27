from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMipLabelAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mipLabelAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.mipLabelAuditRecord")



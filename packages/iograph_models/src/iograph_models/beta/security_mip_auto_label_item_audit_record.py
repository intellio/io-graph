from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMipAutoLabelItemAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mipAutoLabelItemAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.mipAutoLabelItemAuditRecord")



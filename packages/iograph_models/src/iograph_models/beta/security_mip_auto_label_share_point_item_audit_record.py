from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMipAutoLabelSharePointItemAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mipAutoLabelSharePointItemAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.mipAutoLabelSharePointItemAuditRecord")



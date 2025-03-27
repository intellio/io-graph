from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMipAutoLabelSharePointPolicyLocationAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mipAutoLabelSharePointPolicyLocationAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.mipAutoLabelSharePointPolicyLocationAuditRecord")



from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMipExactDataMatchAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mipExactDataMatchAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.mipExactDataMatchAuditRecord")



from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityCustomerKeyServiceEncryptionAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.customerKeyServiceEncryptionAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.customerKeyServiceEncryptionAuditRecord")


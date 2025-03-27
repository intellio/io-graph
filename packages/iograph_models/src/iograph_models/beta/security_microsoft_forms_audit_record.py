from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMicrosoftFormsAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.microsoftFormsAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.microsoftFormsAuditRecord")



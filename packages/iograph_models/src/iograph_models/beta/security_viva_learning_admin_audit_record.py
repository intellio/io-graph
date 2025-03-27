from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityVivaLearningAdminAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.vivaLearningAdminAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.vivaLearningAdminAuditRecord")



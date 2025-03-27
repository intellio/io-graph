from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityTodoAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.todoAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.todoAuditRecord")



from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityLabelContentExplorerAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.labelContentExplorerAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.labelContentExplorerAuditRecord")


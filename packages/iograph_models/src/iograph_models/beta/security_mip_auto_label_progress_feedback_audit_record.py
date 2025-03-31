from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMipAutoLabelProgressFeedbackAuditRecord(BaseModel):
	odata_type: Literal["#microsoft.graph.security.mipAutoLabelProgressFeedbackAuditRecord"] = Field(alias="@odata.type", default="#microsoft.graph.security.mipAutoLabelProgressFeedbackAuditRecord")


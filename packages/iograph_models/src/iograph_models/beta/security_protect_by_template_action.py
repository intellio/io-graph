from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityProtectByTemplateAction(BaseModel):
	odata_type: Literal["#microsoft.graph.security.protectByTemplateAction"] = Field(alias="@odata.type", default="#microsoft.graph.security.protectByTemplateAction")
	templateId: Optional[str] = Field(alias="templateId", default=None,)


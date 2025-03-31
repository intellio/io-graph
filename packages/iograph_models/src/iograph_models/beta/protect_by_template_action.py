from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ProtectByTemplateAction(BaseModel):
	odata_type: Literal["#microsoft.graph.protectByTemplateAction"] = Field(alias="@odata.type", default="#microsoft.graph.protectByTemplateAction")
	templateId: Optional[str] = Field(alias="templateId", default=None,)


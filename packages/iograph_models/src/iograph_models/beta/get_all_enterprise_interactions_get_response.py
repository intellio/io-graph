from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_all_enterprise_interactionsGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AiInteraction]] = Field(alias="value", default=None,)

from .ai_interaction import AiInteraction

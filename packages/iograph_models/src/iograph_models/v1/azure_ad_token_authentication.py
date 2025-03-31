from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AzureAdTokenAuthentication(BaseModel):
	odata_type: Literal["#microsoft.graph.azureAdTokenAuthentication"] = Field(alias="@odata.type", default="#microsoft.graph.azureAdTokenAuthentication")
	resourceId: Optional[str] = Field(alias="resourceId", default=None,)


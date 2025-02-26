from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AzureAdTokenAuthentication(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	resourceId: Optional[str] = Field(default=None,alias="resourceId",)



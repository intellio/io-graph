from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExternalConnectorsConfiguration(BaseModel):
	authorizedAppIds: Optional[list[str]] = Field(default=None,alias="authorizedAppIds",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)



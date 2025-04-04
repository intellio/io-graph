from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExternalConnectorsConfiguration(BaseModel):
	authorizedAppIds: Optional[list[str]] = Field(alias="authorizedAppIds", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


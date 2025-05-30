from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ExternalSponsors(BaseModel):
	isBackup: Optional[bool] = Field(alias="isBackup", default=None,)
	odata_type: Literal["#microsoft.graph.externalSponsors"] = Field(alias="@odata.type", default="#microsoft.graph.externalSponsors")


from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ExactMatchUploadAgent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.exactMatchUploadAgent"] = Field(alias="@odata.type",)
	creationDateTime: Optional[datetime] = Field(alias="creationDateTime", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)


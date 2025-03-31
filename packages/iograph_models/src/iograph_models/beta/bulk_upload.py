from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class BulkUpload(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.bulkUpload"] = Field(alias="@odata.type",)


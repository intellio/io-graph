from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class FileClassificationRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.fileClassificationRequest"] = Field(alias="@odata.type", default="#microsoft.graph.fileClassificationRequest")
	file: Optional[str] = Field(alias="file", default=None,)
	sensitiveTypeIds: Optional[list[str]] = Field(alias="sensitiveTypeIds", default=None,)


from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class DocumentSetVersionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[DocumentSetVersion] = Field(alias="value",)

from .document_set_version import DocumentSetVersion


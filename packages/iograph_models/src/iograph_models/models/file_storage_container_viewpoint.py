from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FileStorageContainerViewpoint(BaseModel):
	effectiveRole: Optional[str] = Field(default=None,alias="effectiveRole",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)



from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FileStorageContainerViewpoint(BaseModel):
	effectiveRole: Optional[str] = Field(alias="effectiveRole",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)



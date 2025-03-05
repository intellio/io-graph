from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MediaInfo(BaseModel):
	resourceId: Optional[str] = Field(default=None,alias="resourceId",)
	uri: Optional[str] = Field(default=None,alias="uri",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)



from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ServiceHostedMediaConfig(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	preFetchMedia: Optional[list[MediaInfo]] = Field(alias="preFetchMedia",default=None,)

from .media_info import MediaInfo


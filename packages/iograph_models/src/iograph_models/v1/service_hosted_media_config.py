from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ServiceHostedMediaConfig(BaseModel):
	odata_type: Literal["#microsoft.graph.serviceHostedMediaConfig"] = Field(alias="@odata.type", default="#microsoft.graph.serviceHostedMediaConfig")
	preFetchMedia: Optional[list[MediaInfo]] = Field(alias="preFetchMedia", default=None,)

from .media_info import MediaInfo

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RedirectUriSettingsCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[RedirectUriSettings] = Field(alias="value",)

from .redirect_uri_settings import RedirectUriSettings


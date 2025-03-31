from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CustomExtensionClientConfiguration(BaseModel):
	maximumRetries: Optional[int] = Field(alias="maximumRetries", default=None,)
	timeoutInMilliseconds: Optional[int] = Field(alias="timeoutInMilliseconds", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


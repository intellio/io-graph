from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnTokenIssuanceStartCustomExtensionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[OnTokenIssuanceStartCustomExtension] = Field(alias="value",)

from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension


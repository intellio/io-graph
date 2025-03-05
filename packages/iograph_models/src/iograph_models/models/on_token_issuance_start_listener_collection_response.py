from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnTokenIssuanceStartListenerCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[OnTokenIssuanceStartListener]] = Field(default=None,alias="value",)

from .on_token_issuance_start_listener import OnTokenIssuanceStartListener


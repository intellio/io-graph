from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnTokenIssuanceStartReturnClaimCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[OnTokenIssuanceStartReturnClaim]] = Field(alias="value",default=None,)

from .on_token_issuance_start_return_claim import OnTokenIssuanceStartReturnClaim


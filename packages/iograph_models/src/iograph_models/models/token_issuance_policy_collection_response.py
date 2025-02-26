from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TokenIssuancePolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[TokenIssuancePolicy] = Field(alias="value",)

from .token_issuance_policy import TokenIssuancePolicy


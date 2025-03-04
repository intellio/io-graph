from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_relying_party_detailed_summary_with_periodGetResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[RelyingPartyDetailedSummary]] = Field(default=None,alias="value",)

from .relying_party_detailed_summary import RelyingPartyDetailedSummary


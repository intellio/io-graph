from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_relying_party_detailed_summary_with_periodGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[RelyingPartyDetailedSummary]] = Field(alias="value",default=None,)

from .relying_party_detailed_summary import RelyingPartyDetailedSummary


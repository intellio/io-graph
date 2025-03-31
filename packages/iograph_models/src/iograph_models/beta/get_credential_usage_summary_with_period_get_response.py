from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_credential_usage_summary_with_periodGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[CredentialUsageSummary]] = Field(alias="value", default=None,)

from .credential_usage_summary import CredentialUsageSummary

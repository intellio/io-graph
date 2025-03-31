from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityAnalyzedEmailExchangeTransportRuleInfoCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecurityAnalyzedEmailExchangeTransportRuleInfo]] = Field(alias="value", default=None,)

from .security_analyzed_email_exchange_transport_rule_info import SecurityAnalyzedEmailExchangeTransportRuleInfo

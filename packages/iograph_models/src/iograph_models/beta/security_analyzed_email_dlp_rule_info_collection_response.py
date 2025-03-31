from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SecurityAnalyzedEmailDlpRuleInfoCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SecurityAnalyzedEmailDlpRuleInfo]] = Field(alias="value", default=None,)

from .security_analyzed_email_dlp_rule_info import SecurityAnalyzedEmailDlpRuleInfo

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class NetworkaccessWebCategoriesSummary(BaseModel):
	action: Optional[NetworkaccessFilteringPolicyAction | str] = Field(alias="action", default=None,)
	deviceCount: Optional[int] = Field(alias="deviceCount", default=None,)
	transactionCount: Optional[int] = Field(alias="transactionCount", default=None,)
	userCount: Optional[int] = Field(alias="userCount", default=None,)
	webCategory: Optional[NetworkaccessWebCategory] = Field(alias="webCategory", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .networkaccess_filtering_policy_action import NetworkaccessFilteringPolicyAction
from .networkaccess_web_category import NetworkaccessWebCategory

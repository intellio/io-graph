from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Win32LobAppProductCodeRule(BaseModel):
	ruleType: Optional[Win32LobAppRuleType] = Field(default=None,alias="ruleType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	productCode: Optional[str] = Field(default=None,alias="productCode",)
	productVersion: Optional[str] = Field(default=None,alias="productVersion",)
	productVersionOperator: Optional[Win32LobAppRuleOperator] = Field(default=None,alias="productVersionOperator",)

from .win32_lob_app_rule_type import Win32LobAppRuleType
from .win32_lob_app_rule_operator import Win32LobAppRuleOperator


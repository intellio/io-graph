from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobAppProductCodeRule(BaseModel):
	ruleType: Optional[str | Win32LobAppRuleType] = Field(alias="ruleType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	productCode: Optional[str] = Field(alias="productCode",default=None,)
	productVersion: Optional[str] = Field(alias="productVersion",default=None,)
	productVersionOperator: Optional[str | Win32LobAppRuleOperator] = Field(alias="productVersionOperator",default=None,)

from .win32_lob_app_rule_type import Win32LobAppRuleType
from .win32_lob_app_rule_operator import Win32LobAppRuleOperator


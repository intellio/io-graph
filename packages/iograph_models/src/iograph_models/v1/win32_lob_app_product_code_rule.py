from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Win32LobAppProductCodeRule(BaseModel):
	ruleType: Optional[Win32LobAppRuleType | str] = Field(alias="ruleType", default=None,)
	odata_type: Literal["#microsoft.graph.win32LobAppProductCodeRule"] = Field(alias="@odata.type", default="#microsoft.graph.win32LobAppProductCodeRule")
	productCode: Optional[str] = Field(alias="productCode", default=None,)
	productVersion: Optional[str] = Field(alias="productVersion", default=None,)
	productVersionOperator: Optional[Win32LobAppRuleOperator | str] = Field(alias="productVersionOperator", default=None,)

from .win32_lob_app_rule_type import Win32LobAppRuleType
from .win32_lob_app_rule_operator import Win32LobAppRuleOperator

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobAppFileSystemRule(BaseModel):
	ruleType: Optional[Win32LobAppRuleType | str] = Field(alias="ruleType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	check32BitOn64System: Optional[bool] = Field(alias="check32BitOn64System",default=None,)
	comparisonValue: Optional[str] = Field(alias="comparisonValue",default=None,)
	fileOrFolderName: Optional[str] = Field(alias="fileOrFolderName",default=None,)
	operationType: Optional[Win32LobAppFileSystemOperationType | str] = Field(alias="operationType",default=None,)
	operator: Optional[Win32LobAppRuleOperator | str] = Field(alias="operator",default=None,)
	path: Optional[str] = Field(alias="path",default=None,)

from .win32_lob_app_rule_type import Win32LobAppRuleType
from .win32_lob_app_file_system_operation_type import Win32LobAppFileSystemOperationType
from .win32_lob_app_rule_operator import Win32LobAppRuleOperator


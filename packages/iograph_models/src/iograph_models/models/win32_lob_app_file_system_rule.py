from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobAppFileSystemRule(BaseModel):
	ruleType: Optional[Win32LobAppRuleType] = Field(default=None,alias="ruleType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	check32BitOn64System: Optional[bool] = Field(default=None,alias="check32BitOn64System",)
	comparisonValue: Optional[str] = Field(default=None,alias="comparisonValue",)
	fileOrFolderName: Optional[str] = Field(default=None,alias="fileOrFolderName",)
	operationType: Optional[Win32LobAppFileSystemOperationType] = Field(default=None,alias="operationType",)
	operator: Optional[Win32LobAppRuleOperator] = Field(default=None,alias="operator",)
	path: Optional[str] = Field(default=None,alias="path",)

from .win32_lob_app_rule_type import Win32LobAppRuleType
from .win32_lob_app_file_system_operation_type import Win32LobAppFileSystemOperationType
from .win32_lob_app_rule_operator import Win32LobAppRuleOperator


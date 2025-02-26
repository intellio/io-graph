from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RegistryKeyState(BaseModel):
	hive: Optional[RegistryHive] = Field(default=None,alias="hive",)
	key: Optional[str] = Field(default=None,alias="key",)
	oldKey: Optional[str] = Field(default=None,alias="oldKey",)
	oldValueData: Optional[str] = Field(default=None,alias="oldValueData",)
	oldValueName: Optional[str] = Field(default=None,alias="oldValueName",)
	operation: Optional[RegistryOperation] = Field(default=None,alias="operation",)
	processId: Optional[int] = Field(default=None,alias="processId",)
	valueData: Optional[str] = Field(default=None,alias="valueData",)
	valueName: Optional[str] = Field(default=None,alias="valueName",)
	valueType: Optional[RegistryValueType] = Field(default=None,alias="valueType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .registry_hive import RegistryHive
from .registry_operation import RegistryOperation
from .registry_value_type import RegistryValueType


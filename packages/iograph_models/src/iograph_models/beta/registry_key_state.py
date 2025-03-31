from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class RegistryKeyState(BaseModel):
	hive: Optional[RegistryHive | str] = Field(alias="hive", default=None,)
	key: Optional[str] = Field(alias="key", default=None,)
	oldKey: Optional[str] = Field(alias="oldKey", default=None,)
	oldValueData: Optional[str] = Field(alias="oldValueData", default=None,)
	oldValueName: Optional[str] = Field(alias="oldValueName", default=None,)
	operation: Optional[RegistryOperation | str] = Field(alias="operation", default=None,)
	processId: Optional[int] = Field(alias="processId", default=None,)
	valueData: Optional[str] = Field(alias="valueData", default=None,)
	valueName: Optional[str] = Field(alias="valueName", default=None,)
	valueType: Optional[RegistryValueType | str] = Field(alias="valueType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .registry_hive import RegistryHive
from .registry_operation import RegistryOperation
from .registry_value_type import RegistryValueType

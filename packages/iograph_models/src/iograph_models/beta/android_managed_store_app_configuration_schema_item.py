from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidManagedStoreAppConfigurationSchemaItem(BaseModel):
	dataType: Optional[AndroidManagedStoreAppConfigurationSchemaItemDataType | str] = Field(alias="dataType",default=None,)
	defaultBoolValue: Optional[bool] = Field(alias="defaultBoolValue",default=None,)
	defaultIntValue: Optional[int] = Field(alias="defaultIntValue",default=None,)
	defaultStringArrayValue: Optional[list[str]] = Field(alias="defaultStringArrayValue",default=None,)
	defaultStringValue: Optional[str] = Field(alias="defaultStringValue",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	index: Optional[int] = Field(alias="index",default=None,)
	parentIndex: Optional[int] = Field(alias="parentIndex",default=None,)
	schemaItemKey: Optional[str] = Field(alias="schemaItemKey",default=None,)
	selections: Optional[list[KeyValuePair]] = Field(alias="selections",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .android_managed_store_app_configuration_schema_item_data_type import AndroidManagedStoreAppConfigurationSchemaItemDataType
from .key_value_pair import KeyValuePair


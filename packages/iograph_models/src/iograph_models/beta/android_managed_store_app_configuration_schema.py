from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidManagedStoreAppConfigurationSchema(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	exampleJson: Optional[str] = Field(alias="exampleJson", default=None,)
	nestedSchemaItems: Optional[list[AndroidManagedStoreAppConfigurationSchemaItem]] = Field(alias="nestedSchemaItems", default=None,)
	schemaItems: Optional[list[AndroidManagedStoreAppConfigurationSchemaItem]] = Field(alias="schemaItems", default=None,)

from .android_managed_store_app_configuration_schema_item import AndroidManagedStoreAppConfigurationSchemaItem
from .android_managed_store_app_configuration_schema_item import AndroidManagedStoreAppConfigurationSchemaItem


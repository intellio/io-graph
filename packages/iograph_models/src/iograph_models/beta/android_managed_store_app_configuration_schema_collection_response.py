from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AndroidManagedStoreAppConfigurationSchemaCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AndroidManagedStoreAppConfigurationSchema]] = Field(alias="value", default=None,)

from .android_managed_store_app_configuration_schema import AndroidManagedStoreAppConfigurationSchema

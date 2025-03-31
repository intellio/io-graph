from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AndroidForWorkAppConfigurationSchemaItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AndroidForWorkAppConfigurationSchemaItem]] = Field(alias="value", default=None,)

from .android_for_work_app_configuration_schema_item import AndroidForWorkAppConfigurationSchemaItem

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidForWorkAppConfigurationSchema(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	exampleJson: Optional[str] = Field(alias="exampleJson", default=None,)
	schemaItems: Optional[list[AndroidForWorkAppConfigurationSchemaItem]] = Field(alias="schemaItems", default=None,)

from .android_for_work_app_configuration_schema_item import AndroidForWorkAppConfigurationSchemaItem


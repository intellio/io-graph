from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AndroidForWorkAppConfigurationSchema(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.androidForWorkAppConfigurationSchema"] = Field(alias="@odata.type",)
	exampleJson: Optional[str] = Field(alias="exampleJson", default=None,)
	schemaItems: Optional[list[AndroidForWorkAppConfigurationSchemaItem]] = Field(alias="schemaItems", default=None,)

from .android_for_work_app_configuration_schema_item import AndroidForWorkAppConfigurationSchemaItem

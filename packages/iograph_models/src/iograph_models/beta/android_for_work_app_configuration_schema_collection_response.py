from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidForWorkAppConfigurationSchemaCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AndroidForWorkAppConfigurationSchema]] = Field(alias="value", default=None,)

from .android_for_work_app_configuration_schema import AndroidForWorkAppConfigurationSchema


from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ContentCustomization(BaseModel):
	attributeCollection: Optional[list[KeyValue]] = Field(alias="attributeCollection",default=None,)
	attributeCollectionRelativeUrl: Optional[str] = Field(alias="attributeCollectionRelativeUrl",default=None,)
	registrationCampaign: Optional[list[KeyValue]] = Field(alias="registrationCampaign",default=None,)
	registrationCampaignRelativeUrl: Optional[str] = Field(alias="registrationCampaignRelativeUrl",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .key_value import KeyValue
from .key_value import KeyValue


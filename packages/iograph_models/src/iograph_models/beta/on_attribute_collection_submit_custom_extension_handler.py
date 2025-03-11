from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnAttributeCollectionSubmitCustomExtensionHandler(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	configuration: Optional[CustomExtensionOverwriteConfiguration] = Field(alias="configuration",default=None,)
	customExtension: Optional[OnAttributeCollectionSubmitCustomExtension] = Field(alias="customExtension",default=None,)

from .custom_extension_overwrite_configuration import CustomExtensionOverwriteConfiguration
from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension


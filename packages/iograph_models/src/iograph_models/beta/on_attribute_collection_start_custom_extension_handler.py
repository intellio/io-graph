from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class OnAttributeCollectionStartCustomExtensionHandler(BaseModel):
	odata_type: Literal["#microsoft.graph.onAttributeCollectionStartCustomExtensionHandler"] = Field(alias="@odata.type", default="#microsoft.graph.onAttributeCollectionStartCustomExtensionHandler")
	configuration: Optional[CustomExtensionOverwriteConfiguration] = Field(alias="configuration", default=None,)
	customExtension: Optional[OnAttributeCollectionStartCustomExtension] = Field(alias="customExtension", default=None,)

from .custom_extension_overwrite_configuration import CustomExtensionOverwriteConfiguration
from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension


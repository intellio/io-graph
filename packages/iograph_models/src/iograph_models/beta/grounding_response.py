from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class GroundingResponse(BaseModel):
	extracts: Optional[list[str]] = Field(alias="extracts",default=None,)
	resourceMetadata: Optional[SearchResourceMetadataDictionary] = Field(alias="resourceMetadata",default=None,)
	resourceType: Optional[GroundingEntityType | str] = Field(alias="resourceType",default=None,)
	sensitivityLabel: Optional[SearchSensitivityLabelInfo] = Field(alias="sensitivityLabel",default=None,)
	webUrl: Optional[str] = Field(alias="webUrl",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .search_resource_metadata_dictionary import SearchResourceMetadataDictionary
from .grounding_entity_type import GroundingEntityType
from .search_sensitivity_label_info import SearchSensitivityLabelInfo


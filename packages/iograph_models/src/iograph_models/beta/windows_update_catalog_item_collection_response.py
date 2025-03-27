from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdateCatalogItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[WindowsFeatureUpdateCatalogItem, WindowsQualityUpdateCatalogItem],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .windows_feature_update_catalog_item import WindowsFeatureUpdateCatalogItem
from .windows_quality_update_catalog_item import WindowsQualityUpdateCatalogItem


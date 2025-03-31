from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class BaseItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[SitePage, Drive, DriveItem, List, ListItem, RecycleBin, RecycleBinItem, SharedDriveItem, Site],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .site_page import SitePage
from .drive import Drive
from .drive_item import DriveItem
from .list import List
from .list_item import ListItem
from .recycle_bin import RecycleBin
from .recycle_bin_item import RecycleBinItem
from .shared_drive_item import SharedDriveItem
from .site import Site

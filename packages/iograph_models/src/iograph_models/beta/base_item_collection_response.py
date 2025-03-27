from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class BaseItemCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[BaseSitePage, NewsLinkPage, PageTemplate, SitePage, VideoNewsLinkPage, Drive, DriveItem, List, ListItem, RecycleBin, RecycleBinItem, SharedDriveItem, Site],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .base_site_page import BaseSitePage
from .news_link_page import NewsLinkPage
from .page_template import PageTemplate
from .site_page import SitePage
from .video_news_link_page import VideoNewsLinkPage
from .drive import Drive
from .drive_item import DriveItem
from .list import List
from .list_item import ListItem
from .recycle_bin import RecycleBin
from .recycle_bin_item import RecycleBinItem
from .shared_drive_item import SharedDriveItem
from .site import Site


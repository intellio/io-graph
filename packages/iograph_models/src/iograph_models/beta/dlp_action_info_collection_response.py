from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class DlpActionInfoCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[BlockAccessAction, NotifyUserAction],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .block_access_action import BlockAccessAction
from .notify_user_action import NotifyUserAction

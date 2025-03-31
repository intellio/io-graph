from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class AccessReviewApplyActionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[DisableAndDeleteUserApplyAction, RemoveAccessApplyAction],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .disable_and_delete_user_apply_action import DisableAndDeleteUserApplyAction
from .remove_access_apply_action import RemoveAccessApplyAction

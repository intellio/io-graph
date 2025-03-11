from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConfigurationManagerAction(BaseModel):
	action: Optional[ConfigurationManagerActionType | str] = Field(alias="action",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .configuration_manager_action_type import ConfigurationManagerActionType


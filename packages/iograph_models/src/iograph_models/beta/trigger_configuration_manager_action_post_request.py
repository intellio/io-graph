from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Trigger_configuration_manager_actionPostRequest(BaseModel):
	configurationManagerAction: Optional[ConfigurationManagerAction] = Field(alias="configurationManagerAction", default=None,)

from .configuration_manager_action import ConfigurationManagerAction


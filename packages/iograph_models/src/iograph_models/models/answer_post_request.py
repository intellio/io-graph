from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AnswerPostRequest(BaseModel):
	callbackUri: Optional[str] = Field(alias="callbackUri",default=None,)
	mediaConfig: SerializeAsAny[Optional[MediaConfig]] = Field(alias="mediaConfig",default=None,)
	acceptedModalities: Optional[str | Modality] = Field(alias="acceptedModalities",default=None,)
	participantCapacity: Optional[int] = Field(alias="participantCapacity",default=None,)
	callOptions: Optional[IncomingCallOptions] = Field(alias="callOptions",default=None,)

from .media_config import MediaConfig
from .modality import Modality
from .incoming_call_options import IncomingCallOptions


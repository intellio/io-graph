from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field


class AnswerPostRequest(BaseModel):
	callbackUri: Optional[str] = Field(alias="callbackUri", default=None,)
	mediaConfig: Optional[Union[AppHostedMediaConfig, ServiceHostedMediaConfig]] = Field(alias="mediaConfig", default=None,discriminator="odata_type", )
	acceptedModalities: Optional[list[Modality | str]] = Field(alias="acceptedModalities", default=None,)
	participantCapacity: Optional[int] = Field(alias="participantCapacity", default=None,)
	callOptions: Optional[IncomingCallOptions] = Field(alias="callOptions", default=None,)

from .app_hosted_media_config import AppHostedMediaConfig
from .service_hosted_media_config import ServiceHostedMediaConfig
from .modality import Modality
from .incoming_call_options import IncomingCallOptions
